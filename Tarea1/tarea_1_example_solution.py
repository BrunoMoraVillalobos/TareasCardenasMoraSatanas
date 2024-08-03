def operation_selector(num1, num2, op):
    if not (isinstance(num1, int) and isinstance(num2, int)):  # Verificar que
        # num1 y num2 sean enteros
        return -50, None  # error 1: num1 o num2 no son enteros
    elif not isinstance(op, str):  # Verifica la existencia de un string
        return -60, None  # error 2: op no es un string
    elif op not in {'+', '-', '*', '&'}:  # Se asegura de que se emplee
        # una de las operaciones asignadas
        return -70, None  # error 3: op no es una opción permitida
    elif (isinstance(num1, bool) or isinstance(num2, bool)):
        return -50, None  # error 1: num1 o num2 no son enteros
    else:
        operations = {
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '&': num1 & num2}
        return 0, operations[op]  # Devuelve el resultado de la operación


def calculo_promedio(lista_valores):
    if not isinstance(lista_valores, list):  # Verifica que
        # lista_valores sea una lista
        return -40, None  # error 1: lista_valores no es una lista
    elif len(lista_valores) > 10:  # Revisa que la lista
        # no tenga más de 10 elementos
        return -90, None  # error 2: lista_valores tiene más de 10 elementos
    elif not all(isinstance(valor, (int, float)) for valor in lista_valores):
        # Se asegura de que los elementos de la lista sean números
        return -80, None  # error 3: algún elemento no es un número
    for valor in lista_valores:
        if isinstance(valor, bool):  # Se asegura de que
            # los elementos de la lista sean números
            return -80, None  # error 3: algún elemento no es un número
    else:
        return 0, (sum(lista_valores)/len(lista_valores))
