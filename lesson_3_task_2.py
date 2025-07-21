from lesson_1.smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S23", "+79007654321"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79009876543"),
    Smartphone("Huawei", "P50 Pro", "+79006543210"),
    Smartphone("OnePlus", "9 Pro", "+79005432109"),
]

for self in catalog:
    print(f"{self.marka} - {self.model}. {self.number}")
