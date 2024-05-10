
usuarios = []

usuario = []

i = 0

while len(usuarios) < 5:

    
    nombre = input("Ingresa el nombre: ")
    usuario.append(nombre)
    apellido = input("Ingresa el apellido: ")
    usuario.append(apellido)
    telefono= input("Ingresa el telefono: ")
    usuario.append(telefono)
    mail = input("Ingresa el correo: ")
    usuario.append(mail)
    clave = input("Ingresa la clave: ")
    usuario.append(clave)
    i += 1
    usuarios.append(usuario[i])


print(usuarios[0], "\n")
print("______________________________________________________________________________________________________")
print(usuarios[1])
print("______________________________________________________________________________________________________")
print(usuarios[2])
print("______________________________________________________________________________________________________")
print(usuarios[3])
print("______________________________________________________________________________________________________")
print(usuarios[4])
print("______________________________________________________________________________________________________")
print(usuarios[5])
print("______________________________________________________________________________________________________")