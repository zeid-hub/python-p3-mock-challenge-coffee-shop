# class Coffee:
#     def __init__(self, name):
#         self.name = name
        
#     def orders(self):
#         pass
    
#     def customers(self):
#         pass
    
#     def num_orders(self):
#         pass
    
#     def average_price(self):
#         pass

# class Customer:
#     def __init__(self, name):
#         self.name = name
        
#     def orders(self):
#         pass
    
#     def coffees(self):
#         pass
    
#     def create_order(self, coffee, price):
#         pass
    
# class Order:
#     def __init__(self, customer, coffee, price):
#         self.customer = customer
#         self.coffee = coffee
#         self.price = price

# class Coffee:
#     def __init__(self, name):
#         self.name = name
#         self._orders = []

#     def orders(self):
#         return self._orders

#     def customers(self):
#         return list(set(order.customer for order in self._orders))

#     def num_orders(self):
#         return len(self._orders)

#     def average_price(self):
#         if not self._orders:
#             return 0
#         total_price = sum(order.price for order in self._orders)
#         return total_price / len(self._orders)


# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self._orders = []

#     def orders(self):
#         return self._orders

#     def coffees(self):
#         return list(set(order.coffee for order in self._orders))

#     def create_order(self, coffee, price):
#         order = Order(self, coffee, price)
#         self._orders.append(order)
#         return order


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer._orders.append(self)
        coffee._orders.append(self)



class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Invalid name for coffee")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Invalid name for customer")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

