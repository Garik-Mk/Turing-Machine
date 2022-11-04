
def cantor_pairing_function(vector: tuple) -> int:
    x, y = vector
    
    number = (x + y + 1) * (x + y)
    number //= 2
    number += y
    
    return number


def cantor_pairing_inverted(number: int) -> tuple:
    pass

class Godel_numbering():
    def __init__(self) -> None:
        pass


cantor_pairing_function((10, 20))