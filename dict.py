

producto = {"id":1, "nombre":"Alpinito","precio":1500, "cantidad": 20,"estado":"disponible"}

print(producto["nombre"])

producto.update({"cantidad":15})

print(producto["cantidad"])

print(len(producto))

for key, value in producto.items():
    print(key,value)

usuario = {}

id_user = int(input("ingrese el id"))
usuario.update({"id": id_user})

name_user = input("Nombre")
usuario.update({"nombre":name_user})

email_user = input("corre")
usuario.update({"mail": email_user})

clave_user = input("clave: ")
usuario.update({"clave": clave_user})

print(usuario)

usuario.popitem()

print(usuario)
