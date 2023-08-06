from rich import print as rprint

from items import Item, ItemQuality, WeaponClass

if __name__ == "__main__":
    item = Item()
    item.name = "Sword"
    # item.quality = ItemQuality.NORMAL
    item.item_class = WeaponClass.SWORD

    for quality in ItemQuality:
        item.quality = quality
        rprint(f"{str(item)} ({item.quality.name})")
