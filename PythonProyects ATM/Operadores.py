#Calcular el diametro de una circunferencia
pi = 3.1416
circunferencia = int(input("Cual es el tamaño de la circuferencia "))

diametro = circunferencia / pi
print(f"El diametro es: {diametro}")
radio = circunferencia / (2*pi)
print(f"EL radio de un circulo de circuferencia{circunferencia} es {radio}")

circunferencia2 = 103
es_mayor = circunferencia2 >= circunferencia
print(type(es_mayor))
print(es_mayor)

es_mayor = radio > diametro
print(es_mayor)

son_grandes = (circunferencia and circunferencia2) >= 100
print(son_grandes)

son_grandes = (circunferencia or circunferencia2) <= 100
print(son_grandes)

#Operadores de asignación

salario = 1300000
aux_transp = 160200

salario += aux_transp
print(salario)

#Hallar area


lado = 20

def calcular_area(lado):
    lado *= 4
    return lado 

area = calcular_area(lado)
print(area)

alto = int(input("Ingrese el alto: "))
ancho = int(input("Ingrese el ancho: "))

def calcular_area_rectangulo(ancho, alto):
    ancho*=2
    alto*=2
    area = ancho + alto
    return area

area_rectangulo = calcular_area_rectangulo(alto, ancho)
print(area_rectangulo)