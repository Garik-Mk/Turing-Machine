from math import sqrt

def cantor_pairing_function(x: int, y: int) -> int:
    number = (x + y + 1) * (x + y)
    number //= 2
    number += y
    return number


def cantor_pairing_inverted(number: int) -> tuple:
    w = 8 * number + 1
    w = sqrt(w)
    w -= 1
    w //= 2

    t = w**2 + w
    t /= 2

    y = int(number - t)
    x = int(w - y)

    return (x, y)


class Godel_numbering():
    def __init__(self) -> None:
        pass
