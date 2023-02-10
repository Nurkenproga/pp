from itertools import permutations

def permutation(s):
    a = list(permutations(s))
    for i in a:
        print(i)

b = input()
permutation(b)