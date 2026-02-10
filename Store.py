class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.tovar = {}

    def add(self, tovar_name, price):
        self.tovar[tovar_name] = price

    def remove(self, tovar_name):
        if tovar_name in self.tovar:
            del self.tovar[tovar_name]

    def price(self, tovar_name):
        return self.tovar.get(tovar_name)

    def update_price(self, tovar_name, new_price):
        if tovar_name in self.tovar:
            self.tovar[tovar_name] = new_price


store1 = Store("Fresh Market", "ул. Ленина")
store1.add("apples", 0.5)
store1.add("bananas", 0.75)



print(f'цена товара:',str(store1.price("apples"))+'$')      # 0.5
store1.update_price("apples", 0.55)
print(store1.price("apples"))      # 0.55


store2 = Store("Tech Store", "ул.Победы")
store2.add("laptop", 1200)
store2.add("mouse", 25)
store2.add("keyboard", 45)
store2.remove("mouse")
print(store2.price("mouse"))
