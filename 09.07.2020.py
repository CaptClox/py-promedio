arch = open("archivo_ejemplo.txt", "r")
notas_dict = dict()  # {}

print(arch.readline())
print(arch.readline())

"""
botar = arch.readline()# botamos la primera linea
for  linea in arch:
    linea_limpia = linea.strip()
    # separacion del nombre de las notas
    linea_limpia_L = (linea_limpia.split(","))
    campo_nombre = linea_limpia_L[0]
    #notas = linea_limpia_L[1:]
    notas = linea_limpia_L[1:len(linea_limpia_L)]
    print("nombre ->",campo_nombre)
    print("notas ->",notas)
    #alt1
    #lista_notas = map(int, notas)
    #promedio_alum =sum(lista_notas)/len(linea_notas)
    #alt2
    promedio_alum = sum(map(int, notas))/3
    #agregar not de alumnos al dicc. notas
    
    #alt3
    #sabemos que notas  tiene almac. una lista de str
    suma_notas = 0
    for i in notas:
        print("nota_i->", i)
        suma_notas = suma_notas + int(i)
    promedio_alum = suma_notas /3
    
    print("promedio alumnos->",promedio_alum)"""
arch.close()
