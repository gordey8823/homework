class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)

import math
print(complex(1, 2)+complex(2, 3))
print(complex(1, 2)*complex(2, 3))
