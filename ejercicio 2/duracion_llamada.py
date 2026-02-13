# Programa calcular costo de una llamada

# input
min = int(input("Digite la duración de la llamada en minutos: "))

# processing
if (min <= 3):
    costo_llamada = 500
else:
    costo_llamada = 500 + (min - 3)*100

# output
print("Duracion de la llamada: " + str(min))
print("costo de llamada: " + str(costo_llamada))
