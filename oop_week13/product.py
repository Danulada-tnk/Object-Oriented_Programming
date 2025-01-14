class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock
    def updatePrice(self, amount):
        self.__price = amount
        return self.__price
    def addStock(self, amount):
        if amount > 0:
            self.__stock += amount
        else:
            print("ไม่สามารถเพิ่มสินค้าได้")
    def discountStock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
        else:
            print("ไม่สามารถลดสินค้าได้")
    def checkProduct(self):
        return f"ชื่อ : {self.name}\nราคาสินค้า : {self.__price}\nจำนวนสินค้า : {self.__stock}"
    
class Phone(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand
    def checkProduct(self):
        return f"ค่าย {self.brand} {super().checkProduct()}"
class notebook(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand
    def checkProduct(self):
        return f"ค่าย {self.brand} {super().checkProduct()}"
class Clothes(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand
    def checkProduct(self):
        return f"ค่าย {self.brand} {super().checkProduct()}"


phone1 = Phone("samsung a 23 5g", 5000,10,"samsung")
notebook1 = notebook ("acer nito v 15",23000,10,"acer")
Clothes1 = Clothes ("adidas original",4000,10,"adidas")
print(Clothes1.checkProduct())  
