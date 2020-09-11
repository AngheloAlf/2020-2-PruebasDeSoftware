from datetime import datetime


## Lee un archivo con los parametros y resultados esperados, y lo entrega como lista.
## Recibe el nombre del archivo. Este archivo debe estar separado por tabulaciones.
## Todos los elementos de la linea, excepto el último, son los parametros de la función.
## El último elemento es el resultado esperado.
## Retorna una lista de tuplas. Tupla de 2 elementos. El primer elemento es la lista
## de parametros que recibe la función, el segundo es el resultado esperado.
def openTestFile(tests_filename: str) -> list:
    tests_list = []

    test_file = open(tests_filename)
    for l in test_file:
        line = l[:-1].split("\t")
        *params, expected_result = line
        tests_list.append((params, expected_result))
    test_file.close()
    return tests_list


## Función que se encarga de probar la función en cuestión.
## Recibe la función a probar, una lista de tests y el nombre del archivo donde se 
## escribiran los resultados.
## Cada linea del archivo `results_filename` tendrá el resultado obtenido, True o False
## indicando si el obtenido es el esperado, y la fecha y hora de la prueba. Estos datos
## están separados por tabulaciones.
## Retorna nada.
def testFunction(function_to_test, tests_list: list, results_filename: str) -> None:
    tests_results = open(results_filename, "w")
    pattern = "{}\t{}\t{}\n"
    for params, expected in tests_list:
        time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        result = function_to_test(*params)
        tests_results.write(pattern.format(result, expected==result, time))
    tests_results.close()
    return


## En caso de querer testear otro archivo, modificarlo de forma acorde
## en la siguiente linea:
from Tarea1ANCC import compareStrings as function_to_test

tests_list = openTestFile("tests.txt")
testFunction(function_to_test, tests_list, "results.txt")
