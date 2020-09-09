from product import Product

class Store:
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self,id):
        for i in range(len(self.products)):
            if self.products[i][0] == id:
                self.products.pop(i)
        return self

    def inflation(self, percent_increase):
        # for item in self.products:
            # item.
        pass

oranges = Product("orange",.50,"fruit")
apples = Product("apple",1.00,"fruit")
Jefes = Store("Jefe's")
Jefes.add_product(oranges).

for ele in Jefes.products:
    # print(store1.products.print_info())
    ele.print_info()