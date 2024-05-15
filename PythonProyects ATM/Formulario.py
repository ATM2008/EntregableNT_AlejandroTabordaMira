producto = []
campos = 5
i = 0

while i < campos:
    valor = input("Ingrese campo: ")
    producto.append(valor)
    i+=1

for item in producto:
    print(item)


encabezados = ("Id","Nombre","Precio","Cantidad","Categoria")

for item in producto:
    for tag in encabezados:
        print(tag, item)