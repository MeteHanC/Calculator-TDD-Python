class Calculator:

    def __init__(self):
        self.number_types = (int, float, complex)

    def add(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x + y
        else:
            raise ValueError

    def multiply(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x*y
        else:
            raise ValueError

    def sub(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x - y
        else:
            raise ValueError

    def div(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x/y
        else:
            raise ValueError
