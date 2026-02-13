# Programa para verificar si un número es par

# input
print("----------------------------------")
print("------Número para/impar-----------")
print("----------------------------------")
x = int(input("Digite un número: "))

# processing
mod = x%2
if (mod == 0):
    rta = "PAR"
else:
    rta = "IMPAR"

# output
Print("--------------------------------")
print("-----------Resultado------------")
print("--------------------------------")
print("El número" + str(x) + " es " + rta)
