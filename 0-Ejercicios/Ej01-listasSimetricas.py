myArray = ['a', 'b', 'd', 's', 'd', '3', 'a']


def is_symetric(array: list) -> str:
    myArray_copy = array.copy()
    myArray_copy.reverse()
    x = 0

    while x < len(array):
        if myArray_copy[x] != array[x]:
            return 'Asymetric'
        x += 1

    return 'Symetric'


print(is_symetric(myArray))
