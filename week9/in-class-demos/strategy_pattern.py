# ShippingStrategy defines an abstract interface.
class ShippingStrategy:
    def calculate(self, weight):
        pass

# Different shipping types are encapsulated strategies.
class ExpressShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 10

class StandardShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 5

# Strategy object is passed into get_shipping_cost().
def get_shipping_cost(strategy, weight):
    # Dynamically call the right method - Polymorphic
    return strategy.calculate(weight)

print(get_shipping_cost(ExpressShipping(), 3))  # 30
# print(get_shipping_cost(StandardShipping(), 3))  # 30