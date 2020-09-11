## Anghelo Carvajal
## 201473062-4
## Comparador de strings. Versión 1.0

from datetime import datetime


## Recibe 2 strings como parametro
## Retorna el string más largo.
def compareStrings(a: str, b: str) -> str:
    with open("logs.txt", "a") as logs:
        try:
            time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            logs.write(time)
            logs.write(f": compareStrings({a}, {b}) -> ")
            if len(b) > len(a):
                logs.write(f"{b}\n")
                return b
            logs.write(f"{a}\n")
            return a
        except Exception as e:
            logs.write(f"\t\t\tException:\n{e}\n\n")
            return None
