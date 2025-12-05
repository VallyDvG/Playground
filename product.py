class Product:
    """Class that represents a product in a store""" 
    def __init__(self, name: str, price: float, stock: int):# Initialize Product with name, price, and stock
        self.name = name
        self.price = price
        self.stock = stock
        self.money =0
    
    def is_in_stock(self)->bool:
        if self.stock >0:
            return True
        else:
            return False
        
    def sell(self,quantity:float):
        if self.stock > quantity:
            self.stock-=quantity
            self.money=self.price * quantity
        else:
            print(f"You cannot buy {quantity} items, there are left {self.stock} items in stock")
        return self.money

    def product_info(self):
        return f"There are left in stock {self.stock} items of {self.name}."

    def __str__(self):
        return f"Product: {self.name}, {self.stock}"

class Inventory():
    """Class that represents an inventory of products."""
    def __init__(self):
        self.products:dict[str,Product] = {}
    
    def add_product(self,product:Product):
        self.products[product.name] = product

    def show_inventory(self):
        for product in self.products.values():
            print(product.product_info())

    def show_product(self,product_name:str):
        try:
            print(self.products[product_name])   
        except KeyError as e:
            print(f"Product: {e} is not in stock! ")
            #print(e)
    def list_products(self):
        for product in self.products.values():
            print(product.product_info())
            
            


class Bank:
    def __init__(self):
        pass


steak=Product("steak",75.3,15)
milk=Product("milk",7.5,50)
bread=Product("bread",3.5,30)


inventory=Inventory()
inventory.add_product(bread)
inventory.add_product(steak)
inventory.add_product(milk)

inventory.show_product("steak")
steak.sell(2)
inventory.show_product("steak")

# inventory.show_product("milk")

# print(milk.product_info())
# inventory.list_products()
# milk.sell(20)
# # print(milk.product_info())
# inventory.list_products()
