""" Este modulo cuenta con metodos para calcular los impuestos y el total del valor de una venta. """


def calcular_impuesto(valor: int) -> float:
    """
    Calcula el total de impuestos a pagar

    Parametros:
    valor (int): El valor del producto

    Return:
    int: El valor del impuesto
    """
    return valor * 0.19 / 100


def calcular_total(valor: int, cantidad: int) -> float:
    return valor * cantidad
