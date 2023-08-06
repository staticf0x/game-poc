import operator
import random
import re
import time
import tomllib

from items import ArmorClass, ConsumableClass, ItemClass, WeaponClass

Number = int | float

random.seed(time.time())


class Option:
    def __init__(self):
        self.filters = []


class Condition:
    def __init__(self):
        self.options = []


class Variant:
    conditions: list[Condition]
    values: Number | list[Number, Number]


class Attribute:
    name: str = "undefined"
    fmt: str = "undefined"
    value = 0
    value_min = 0
    value_max = 0
    item_classes: list[ItemClass]
    item_types: list
    variants = list[Variant]

    def __init__(self):
        self.item_classes = []
        self.item_types = []
        self.config = {}
        self.variants = []

    def pick_value(self, ilevel: int) -> None:
        operators = {
            ">": operator.gt,
            "<": operator.lt,
            ">=": operator.ge,
            "<=": operator.le,
            "==": operator.eq,
        }

        for variant in self.variants:
            check = []

            for cond in variant.conditions:
                spl = re.split(r"([a-z]+)(>|<|<=|>=)(\d+)", cond)[1:-1]

                assert spl[0] == "ilevel"

                op = operators[spl[1]]
                val = int(spl[2])

                check.append(op(ilevel, val))

            if all(check):
                self.value = random.randint(*variant.values)

                break

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.name}"

    def format(self) -> str:
        return self.fmt.format(
            value=self.value,
            value_min=self.value_min,
            value_max=self.value_max,
        )


class AttributePool:
    def __init__(self) -> None:
        self.attributes = []

    def load(self) -> None:
        with open("attributes.toml", "rb") as f:
            loaded = tomllib.load(f)

        for name, entry in loaded.items():
            attr = Attribute()
            attr.name = name
            attr.fmt = entry["fmt"]

            type_lut = {
                ItemClass.WEAPON: WeaponClass,
                ItemClass.ARMOR: ArmorClass,
            }
            type_lookup = []

            if entry["classes"] is True:
                for c in ItemClass:
                    attr.item_classes.append(c)
            else:
                for class_name in entry["classes"]:
                    for c in ItemClass:
                        if class_name == c.name.lower():
                            attr.item_classes.append(c)
                            type_lookup.extend(list(type_lut[c]))

            if entry["types"] is True:
                for t in type_lookup:
                    attr.item_types.append(t)
            else:
                for type_name in entry["types"]:
                    for t in type_lookup:
                        if type_name == t.name.lower():
                            attr.item_types.append(t)

            for cfg in entry.get("config", []):
                condition, values = cfg

                variant = Variant()
                variant.conditions = condition.split(",")
                variant.values = values

                attr.variants.append(variant)

            self.attributes.append(attr)

    def filter(self, item_class: ItemClass, item_type):
        attrs = self.attributes[:]

        if item_class is not None:
            for attr in attrs[:]:
                if item_class not in attr.item_classes:
                    attrs.remove(attr)

        if item_type is not None:
            for attr in attrs[:]:
                if item_type not in attr.item_types:
                    attrs.remove(attr)

        return attrs


class AttributePicker:
    def __init__(
        self,
        pool: AttributePool,
        size: int,
        ilevel: int,
        item_class: ItemClass,
        item_type,
    ) -> None:
        self.size = size
        self.ilevel = ilevel
        self.item_class = item_class
        self.item_type = item_type
        self.pool = pool

    def pick(self) -> list[Attribute]:
        available_attrs = self.pool.filter(self.item_class, self.item_type)
        picked = []

        for _ in range(min(self.size, len(available_attrs))):
            idx = random.randint(0, len(available_attrs) - 1)

            attr = available_attrs[idx]
            attr.pick_value(self.ilevel)

            picked.append(attr)
            available_attrs.pop(idx)

        return sorted(picked, key=lambda x: x.name)
