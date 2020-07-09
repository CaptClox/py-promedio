#ejemplificaar uso de funcion MAP
palabras = ["hola","juan","curso","programacion","universidad"]
#tarea: contar cantidad de caracteres de cada palabra
"""
conteo_cars = []
for p in palabras:
    cnt_cars = len(p)
    conteo_cars.append(cnt_cars)
"""

conteo_cars = list(map(len,palabras))
print(conteo_cars)