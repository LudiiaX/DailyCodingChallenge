import math
def is_integer_hypotenuse(a, b): return (math.sqrt(a*a+b*b)).is_integer()

print(is_integer_hypotenuse(3, 4))
print(is_integer_hypotenuse(2, 3))
print(is_integer_hypotenuse(5, 12))
print(is_integer_hypotenuse(10, 10))
print(is_integer_hypotenuse(780, 1040))
print(is_integer_hypotenuse(250, 333))