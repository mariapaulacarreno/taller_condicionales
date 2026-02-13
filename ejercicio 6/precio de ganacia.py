# Inicio
print("----------")
print("Bienvenido")
print("----------")

print("---------------------------------------")
p= int(input("Ingrese el valor de el producto"))
print("---------------------------------------")

# Proceso

if p <= 3000:
    Ganancia=p*0.15
else:
    if p > 6000:
        Ganancia= p*0.25
    else:
        Ganancia= 500

# Precio Final

P_c=P+Ganancia

# output
print("------------------------------")
print("La ganancia es: "+str(Ganancia))
print("------------------------------")

print("----------------------------")
print("El precio final es "+str(P_c))
print("----------------------------")