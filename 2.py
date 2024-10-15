'''
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud 
de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar 
el ejercicio (se puede extender)
Nota: utilizar la función len
'''

def get_string(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> str | None:

        longitud = input(mensaje)

        if len(longitud) < minimo or len(longitud) > maximo:
            print(mensaje_error)
            reintentos -= 1

            if reintentos > 0:
                return get_string(mensaje, mensaje_error, minimo, maximo, reintentos)
            else:
                print("Limite de reintentos alcanzado.")
        
        return longitud

# Test
# get_string('Escribe un mensaje de 4 letras: ', 'Error, escribe un mensaje dentro del rango valido', 0, 4, 3)


