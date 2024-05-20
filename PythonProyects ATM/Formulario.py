producto = []
campos = 5
i = 0

while i < campos:
    valor = input("Ingrese campo: ")
    producto.append(valor)
    i+=1

encabezados = ("Id","Nombre","Precio","Cantidad","Categoria")

for encabezado in encabezados:
    print(encabezado, end="\t")
print()
for item in producto:
    print(item, end= "\t" )