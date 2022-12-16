class House:
    def __init__(self, name, area):
        self.name = name
        self.total_area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f"户型：{self.name},总面积：{self.total_area},可用面积：{self.free_area}，家具列表：{self.item_list}"

    def add_item(self, item):
        if self.free_area > item.item_area:
            self.item_list.append(item.name)
            self.free_area -= item.item_area
            print(f"家具添加成功")
        else:
            print("房子太小")


class HouseItem:
    def __init__(self, area, name):
        self.name = name
        self.item_area = area

    def __str__(self):
        return f"家具名字：{self.name},家具占用面积：{self.item_area}"


bed = HouseItem(20, '席梦思')
chair = HouseItem(5, '电竞椅')
deck = HouseItem(15, "桌子")
house = House("平房", 30, )
print(bed)
print(chair)
print(deck)
house.add_item(chair)
house.add_item(deck)
house.add_item(bed)
print(house)
