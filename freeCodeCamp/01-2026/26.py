def fizz_buzz_mini(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%5 == 0:
        return "Buzz"
    elif n%3==0:
        return "Fizz"
    return str(n)

print(fizz_buzz_mini(3))
print(fizz_buzz_mini(4))
print(fizz_buzz_mini(35))
print(fizz_buzz_mini(75))
print(fizz_buzz_mini(98))


# 1 raw challenge:
def fizz_buzz_mini(n):
    return "FizzBuzz" if [n%x for x in [3, 5]] == [0,0] else ("Fizz" if [n%x for x in [3, 5]][0] == 0 else (("Buzz" if [n%x for x in [3, 5]][1] == 0 else str(n))))

print(fizz_buzz_mini(3))
print(fizz_buzz_mini(4))
print(fizz_buzz_mini(35))
print(fizz_buzz_mini(75))
print(fizz_buzz_mini(98))