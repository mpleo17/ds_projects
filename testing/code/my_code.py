import time

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_add(self):
        return self.a + self.b

    def calc_sub(self):
        return self.a - self.b

    def calc_mult(self):
        return self.a * self.b

    def calc_div(self):
        if self.b == 0:
            raise ValueError('The denominator cannot be zero!')
        else:
            return self.a / self.b

    def get_timestamp(self):
        return time.time()