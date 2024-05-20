mercado = []
producto = []
campos = 5
i = 0
NumProducto = 0
ProductosTotales = int(input("cuantos productos vas a llevar? "))

while NumProducto < ProductosTotales: 
    while i < campos:
        valor = input("Ingrese campo: ")
        producto.append(valor)
        i+=1  
    mercado.append(producto)
    NumProducto+=1
    encabezados = ("Id","Nombre","Precio","Cantidad","Categoria")

    for item in producto:
        print(item, end= "\t" )