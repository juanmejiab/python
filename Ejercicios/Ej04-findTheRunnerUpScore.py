# In this challenge, you have to print
# the second highest score of an array
# given by the user. N specify the array length
# and arr takes the values
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lista = list(arr)
    lista.sort()

    while n > 0:
        n -= 1
        if lista[n-1] < lista[n]:
            print(lista[n-1])
            break
