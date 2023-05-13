
#TODO create a basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO add properties
        self.author = author # instance attributes
        self.pages = pages
        self.price = price
        self.__secret = "This us a secrete attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self,amount):
        self._discount = amount


        


#TODO create a instance of the class
b1 = Book("Brave New World","Leo Tolsroy", 1225,39.95)
b2 = Book("War and Peace", "JD Salinger", 234, 29.9)



print(b1.getprice())

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())


print(b2._Book__secret)