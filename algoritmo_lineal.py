import matplotlib.pyplot as plt
def algoritmo_lineal(semilla,a,c,m):
    entero=(a*semilla+c)%m
    r=entero/(m-1)
    return r,entero

cantidad=40
semilla=21
pseudoaleatorios=[]
for i in range(cantidad):
    r,semilla=algoritmo_lineal(semilla=semilla,a=21,c=15,m=31)
    pseudoaleatorios.append(semilla)

print(pseudoaleatorios)
print("Numeros pseudoaleatorios generados a traves del tiempo:")
plt.plot(range(cantidad),pseudoaleatorios, marker="o", color="green")
plt.show()
