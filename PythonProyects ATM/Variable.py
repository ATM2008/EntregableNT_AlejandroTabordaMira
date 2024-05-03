#Notacion snake
name = "Pepito"
last_name = "Perez"
mail = "pepito@mail.com"
salary = 1000000         
Note = 4.5

print (mail)

#Concatenar con +

print("Email: " + mail )

#Concatenar con ,

print("Email:", mail )

#Concatenar con format

print(f"Nombre{name}\nApellido:{last_name}\nMail:{mail}\nSalary:{salary}")

# type = Saber el tpo de variable 

print(type(salary))

#Capturar datos

phone = input("Telefono: ")
print(f"Telefono: {phone}")

aux_transporte = int(input("Ingrese el auxilio d transporte"))
total_salary = salary + aux_transporte
print(F"El salario total es:{total_salary}")

per_loan_discount = 0.3

loan_discount = salary * per_loan_discount

total_salary= salary + aux_transporte - loan_discount

print(f"El salario total es:{total_salary} \nDescuentos:\nPrestamos:{loan_discount}")