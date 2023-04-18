class phone:
    def __init__(self, model, is_touch, size,is_fast_charge, price):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.is_fast_charge = is_fast_charge
        self.price = price
    def is_touchable (self):
        if self.is_touch:
            return True
        else:
            return False
    def is_fast_charge (self):
        if self.is_fast_charge:
            return True
        else:
            return False
class Taplet(phone):
    def super__init__(self, model, is_touch, size, price):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.price = price

# What is super this in 13 ?? and why should I keep it ?