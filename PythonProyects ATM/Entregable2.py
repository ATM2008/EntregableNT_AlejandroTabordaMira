usar = "pp@mail.com"
key = 1234
tel = 3137577184

usuario = input("Usuario: ")
clave = int(input("Clave: "))
telefono = int(input("Telefono: "))

if usuario == usar and   telefono == tel or clave == key :
    print("Bienvenido al sistema")
else:
    print("Credenciales incorrectas")
    