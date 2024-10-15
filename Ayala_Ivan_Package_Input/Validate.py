def validate_range(num:int|float, min:int, max:int) -> bool:

    if num >= min and num <= max:
        retorno = True
    else:
        retorno = False
    
    return retorno

def validate_lenght(longitud:int, max:int) -> bool:

    if longitud <= max:
        retorno = True
    else:
        retorno = False
        
    return retorno