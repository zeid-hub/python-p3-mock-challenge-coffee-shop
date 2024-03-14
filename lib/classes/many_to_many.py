class Coffee:
    def __init__(self, name):
        # Set the name using the property setter
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 3 <= len(name) <= 15:  # Update condition for name length
            self._name = name
        else:
            raise ValueError("Invalid name for coffee")

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if len(self.orders()) == 0:
            return 0
        total = sum([order.price for order in self.orders()])
        return total / len(self.orders())

class Customer:
    def __init__(self, name):
        # Set the name using the property setter
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:  # Update condition for name length
            self._name = name
        else:
            raise ValueError("Invalid name for customer")

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee) or not isinstance(price, (int, float)):
            raise ValueError("Invalid input for creating an order")

        new_order = Order(self, coffee, price)
        return new_order

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee) or not isinstance(price, (int, float)):
            raise ValueError("Invalid input for creating an order")

        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0, inclusive")

        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @classmethod
    def clear_all(cls):
        cls.all = []
