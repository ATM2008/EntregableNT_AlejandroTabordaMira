#Cree un bucle que permita hacer una lista de 5 colores
mi_lista_colores = []

contador_colores = 0

while contador_colores < 5:

    color = input("Agregue un color: ")

    mi_lista_colores.append(color)

    contador_colores+= 1

print(mi_lista_colores)