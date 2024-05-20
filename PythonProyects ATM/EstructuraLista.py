
users = []

user1 = [70100100, "Pepito", "Perez", 3214567890, "pp@mail.com", "M", 29, "1234"]

user2 = [70200200, "Maria", "Perez", 32131200, "mp@mail.com", "F", 35, "1234"]

user3 = [70300300, "Sofia", "Perez", 32198744560, "sp@mail.com", "M", 19, "1234"]

users.append(user1)
users.append(user2)
users.append(user3)

print(users)

for item in users:
    print(item)

#crear un inicio de sesion comparando el valor del correo y contraseña
#ingresando el usuario que ya esta en la base de datos 

userIngreso = input("Ingresa tu usuario: ")
claveIngreso = input("Ingresa tu contraseña: ")

if userIngreso == user1[4] or user2[4] or user3[4] and claveIngreso == user1[7] or user2[7] or user3[7]:
    print("Bienvenido")
else: 
    print("error")

i = int(input("ingrese el index del usuario"))
userIngreso = input("Ingresa tu usuario: ")
claveIngreso = input("Ingresa tu contraseña: ")
if userIngreso == users[i][4] and claveIngreso == user1[i][7]:
    print("Bienvenido")
else: 
    print("error")