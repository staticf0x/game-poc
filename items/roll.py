from attributes import Attribute, AttributePicker, AttributePool
from devtools import debug
from rich import inspect
from rich import print as rprint
from rich.panel import Panel

from items import Armor, ArmorClass, Item, ItemClass, ItemQuality

item = Armor()
item.quality = ItemQuality.MAGIC
item.item_class = ItemClass.ARMOR
item.item_type = ArmorClass.HELMET
item.name = "Shiny Helmet"
item.level = 1

pool = AttributePool()
pool.load()

picker = AttributePicker(
    pool=pool,
    size=2,
    ilevel=5,
    item_class=item.item_class,
    item_type=item.item_type,
)
attrs = picker.pick()
item.attributes = attrs

lines = []
lines.append(f"Class: {item.item_class}")
lines.append(f"Type: {item.item_type}")
lines.append(f"Quality: {item.quality}")
lines.append(f"ilevel: {item.level}")
lines.append("")
lines.extend([attr.format() for attr in item.attributes])

panel = Panel("\n".join(lines), title=str(item))
rprint(panel)
