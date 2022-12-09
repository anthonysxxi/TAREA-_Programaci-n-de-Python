sum=0
n=int(input('ingrese la cantidad de datos:'))
for i in range(n):
    sum+=float(input('ingrese los valores:'))
promedio=sum/n
print('El promedio es:',promedio)