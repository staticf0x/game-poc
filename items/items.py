from dataclasses import dataclass
from enum import Enum


class ItemQuality(Enum):
    POOR = 0
    NORMAL = 1
    MAGIC = 2
    RARE = 3
    UNIQUE = 4
    SET = 5
    QUEST = 6

    def __str__(self) -> str:
        names = {
            self.POOR: "Poor",
            self.NORMAL: "Normal",
            self.MAGIC: "Magic",
            self.RARE: "Rare",
            self.UNIQUE: "Unique",
            self.SET: "Set",
            self.QUEST: "Quest",
        }

        return names[self]

    def color(self) -> str:
        colors = {
            self.POOR: "grey",
            self.NORMAL: "white",
            self.MAGIC: "blue",
            self.RARE: "yellow",
            self.UNIQUE: "orange3",
            self.SET: "green",
            self.QUEST: "cyan",
        }

        return colors[self]


class ItemClass(Enum):
    WEAPON = 0
    ARMOR = 1
    CONSUMABLE = 2

    def __str__(self) -> str:
        names = {
            self.WEAPON: "Weapon",
            self.ARMOR: "Armor",
            self.CONSUMABLE: "Consumable",
        }

        return names[self]


class WeaponClass(Enum):
    SWORD = 0
    SHIELD = 1
    BOW = 2
    QUIVER = 3
    THROWN = 4
    AXE = 5
    DAGGER = 6
    WAND = 7
    STAFF = 8

    def __str__(self) -> str:
        names = {
            self.SWORD: "Sword",
            self.SHIELD: "Shield",
            self.BOW: "Bow",
            self.QUIVER: "Quiver",
            self.THROWN: "Thrown",
            self.AXE: "Axe",
            self.DAGGER: "Dagger",
            self.WAND: "Wand",
            self.STAFF: "Staff",
        }

        return names[self]


class ArmorClass(Enum):
    RING = 0
    AMULET = 1
    LIGHT_ARMOR = 2
    HEAVY_ARMOR = 3
    BOOTS = 4
    GLOVES = 5
    HELMET = 6
    BELT = 7

    def __str__(self) -> str:
        names = {
            self.RING: "Ring",
            self.AMULET: "Amulet",
            self.LIGHT_ARMOR: "Light Armor",
            self.HEAVY_ARMOR: "Heavy Armor",
            self.BOOTS: "Boots",
            self.GLOVES: "Gloves",
            self.HELMET: "Helmet",
            self.BELT: "Belt",
        }

        return names[self]


class ConsumableClass(Enum):
    POTION = 0
    HERB = 1
    COMPONENT = 2

    def __str__(self) -> str:
        names = {
            self.POTION: "Potion",
            self.HERB: "Herb",
            self.COMPONENT: "Component",
        }

        return names[self]


class Item:
    name: str = "undefined"
    item_class: ItemClass = ItemClass.ARMOR
    item_type = None
    quality: ItemQuality = ItemQuality.NORMAL
    level: int = 0

    def __init__(self):
        self.quality = None
        self.attributes = []

    def __str__(self):
        color = self.quality.color()

        return f"[{color}]{self.name}[/{color}]"


class Weapon(Item):
    item_class = ItemClass.WEAPON
    item_type: WeaponClass = WeaponClass.SWORD


class Armor(Item):
    item_class = ItemClass.ARMOR
    item_type: ArmorClass = ArmorClass.RING


class Consumable(Item):
    item_class = ItemClass.CONSUMABLE
    item_type: ConsumableClass = ConsumableClass.POTION
