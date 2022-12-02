from math import sqrt
from machine_core import Machine

def cantor_pair(x: int, y: int) -> int:
    number = (x + y + 1) * (x + y)
    number //= 2
    number += y
    return number


def cantor_invert(number: int) -> list:
    w = 8 * number + 1
    w = sqrt(w)
    w -= 1
    w //= 2

    t = w**2 + w
    t /= 2

    y = int(number - t)
    x = int(w - y)

    return [x, y]


def cantor_of_list(numbers: list) -> int:
    ...


def cantor_list_invert(number: int, depth: int) -> list:
    ...



# Essential functions for numerating
# betta(x1, x2, x3...) = cantor_pairing_function(n--1, cantor_pairing_of_list(x1, x2, x3...))+1 returns int
# 
# 1. ro(x) = godel_number(x) returns godel index of x {ro(x) == betta(x), cantor_pairing_function(x) = x}
# 2. delta(z) = len(godel_number(x1, x2, x3...))
# 3. lambda(i, z) = (x1, x2, x3...)[i]
# 4. fi(x, y) = godel_number(godel_number(x1, x2, x3...), y), x = godel_number(x1, x2, x3...)
# 5. psi(x, y) = godel_number(godel_number(x1, x2, x3...), godel_number(y1, y2, y3...))
# 6. tetta(z, i, j) = godel_number((x1, x2, x3, x4, x5, x6, x7...)[i:j])
# 7. xi(x, y) = godel_number(x, x, x, ... x), len(x, x, x, ... x) = y
#

def godel_number():
    ...