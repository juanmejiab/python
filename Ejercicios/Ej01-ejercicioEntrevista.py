myArray = ['a','b','d','s','d','3','a']

def is_symetric(arreglo:list) -> str:
    copia_myArray = arreglo.copy()
    copia_myArray.reverse()
    x=0

    while x < len(arreglo):
        if copia_myArray[x] != arreglo[x]:
            return 'Asymetric'
        x+=1
        
    return 'Symetric'

print(is_symetric(myArray))