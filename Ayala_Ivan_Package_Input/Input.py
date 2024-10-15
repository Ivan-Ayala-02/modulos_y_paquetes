from Ayala_Ivan_Package_Input.Validate import *

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos: int)-> int | None:
    retorno = None
    if reintentos != 0:
        num = int(input(mensaje))
        if validate_range(num, minimo, maximo):
            retorno = num
        else:
            print(mensaje_error)
            retorno = get_int(mensaje,mensaje_error, minimo, maximo, reintentos-1)
    return retorno


def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos: float)-> float | None:
    retorno = None
    if reintentos != 0:
        num = float(input(mensaje))
        if validate_range(num, minimo, maximo):
            retorno = num
        else:
            print(mensaje_error)
            retorno = get_float(mensaje,mensaje_error, minimo, maximo, reintentos-1)
    return retorno


def get_string(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> str | None:
    retorno = None
    if reintentos != 0:
        cadena = input(mensaje)
        longitud = len(cadena)
        if validate_lenght(longitud, maximo):
            retorno = cadena
        else:
            print(mensaje_error)
            retorno = get_string(mensaje,mensaje_error, maximo, reintentos-1)
    return retorno