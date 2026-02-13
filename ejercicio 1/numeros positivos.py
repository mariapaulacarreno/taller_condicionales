# Programa para verificar si un numero es positivo

# input
print("-------------------------------")
print("------Número positvo-----------")
x = int(input("Digite un número: "))

# processing
if (x>0):
    rta = "POSITIVO"
else:
    rta = "NEGATIVO O CERO"

# output
print("El número" + str(x) + " es " + rta)
