# Se tiene una funcion que toma un dato ingresado por el usuario
# si el dato ingresado es divisible por 3 retrona fizz
# si es divisible por 5 retorna buzz
# si es divisible por 3 y 5 retorna fizz buzz
# si no cumple ninguno de los anteriores retorna el valor ingresado


def fizz_buzz(input: int) -> str:
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return str(input)


print(fizz_buzz(15))
