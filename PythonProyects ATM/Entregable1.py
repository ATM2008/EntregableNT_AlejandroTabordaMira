id = input("id del producto: ")
nombre = input("Nombre del producto:")
descripcion = "¡Ahora en el formato perfecto para compartir con la familia y amigos!"
costo = int(input("Ingrese el costo del producto"))
precio = costo / ((1-0.30)) 
cantidad = input ("Cuantas unidades vas a llevar: ")
estado = input ("El producto esta disponible: ")

print(f" ID:{id}\n Nombre:{nombre}\n Descripcion:{descripcion}\n Cantidad{cantidad}\n Estado{estado} Precio:{precio}\n")