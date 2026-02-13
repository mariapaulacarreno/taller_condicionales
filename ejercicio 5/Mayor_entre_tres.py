# Programa para verificar si entre 3 números cual es el mayor

#input
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el primer numero: "))
n3 = int(input("Ingrese el primer numero: "))

# processing
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# output
print("--------------------------------")
print("-----------Resultado------------")
print("--------------------------------")
print("El número mayor es: ", mayor)
