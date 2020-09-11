# Tarea 1 - Validación y verificación

Tarea para practicar la validación y verificación de casos de prueba.

## Dependencias

- [Python 3](https://www.python.org/downloads/)

## Instrucciones de uso

Para usar la función del requerimiento:

```python
import Tarea1ANCC

Tarea1ANCC.compareStrings("corta", "laaaaarga") # retorna "laaaaarga"
Tarea1ANCC.compareStrings("28", "40") # retorna "28"
Tarea1ANCC.compareStrings("お姉ちゃん", "お兄ちゃん") # retorna "お姉ちゃん"
```

También es posible usar la herramienta `tester.py` para probar un conjunto de casos de prueba de forma automática.

Requiere que exista un archivo llamado `tests.txt`, el cual tiene en cada linea los parámetros a probar y el resultado esperado. Estos datos deben estar separados por tabulaciones.

Genera un archivo llamado `results.txt`, el cual también está separado por tabulaciones. El primer elemento es lo que retornó la función al ejecutarla con los parámetros entregados, luego `True` o `False` si el valor de retorno era el valor esperado, finalmente la fecha y hora de la prueba.

```bash
$ cat tests.txt
corta   larga   corta
ayúdame yo tengo muchos quereceres      donde está la lista     ayúdame yo tengo muchos quereceres
$
$ python3 tester.py
$ cat tests.txt
corta   True    2020-09-11 18:00:37
ayúdame yo tengo muchos quereceres      True    2020-09-11 18:00:37
$
```
