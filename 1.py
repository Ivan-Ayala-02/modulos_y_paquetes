'''
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente 
prototipo

En donde:

    ● mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    ● mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    ● mínimo: valor mínimo admitido (inclusive)
    ● máximo: valor máximo admitido (inclusive)
    ● reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None
Repetir el mismo procedimiento para un dato de tipo float
'''

# a)

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos: int)-> int | None:

    num_int = int(input(mensaje))

    if num_int < minimo or num_int > maximo:
        print(mensaje_error)
        reintentos -= 1
    
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        else:
            print("Limite de reintentos alcanzado.")
            return None
    
    return num_int

# b)

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos: float)-> float | None:
    
    num_float = float(input(mensaje))

    if num_float < minimo or num_float > maximo:
        print(mensaje_error)
        reintentos -= 1

        if reintentos > 0:
            return get_float(mensaje, mensaje_error, minimo, maximo, reintentos)
        else:
            print("Limite de reintentos alcanzado.")
            return None
    
    return num_float

# Test
# get_float('Ingrese un numero entre 1 y 10: ', 'Error, ingrese un num dentro del rango valido', 1, 10, 3)
