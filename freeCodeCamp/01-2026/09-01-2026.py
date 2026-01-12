from itertools import permutations

def is_circular_prime(n):

    perm = permutations(str(n))
    print(perm)

    return n

print(is_circular_prime(197))
print()
print()
print()
