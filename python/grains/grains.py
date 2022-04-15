"""Functions to calculate the number of grains of wheat on a
chessboard given that the number on each square doubles.
"""
def square(number):
    """Calculate how many grains were on a given square

    :param number: the number of square (1, 2, ..., 64).
    :return: int - number of grains on that square.
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number -1)


def total():
    """Calculate the total number of grains on the chessboard

    :return: int - number of grains on the chessboard.
    """
    number_of_grains = 0
    for index in range(1, 65):
        number_of_grains += square(index)
    return number_of_grains
