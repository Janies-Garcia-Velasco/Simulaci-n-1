# -*- coding: utf-8 -*-
"""Copia_de_Actividad_1_cuadrado_medio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Janies-Garcia-Velasco/Simulaci-n-1/blob/main/Copia_de_Actividad_1_cuadrado_medio.ipynb

# Cuadrado medio
"""

import tabulate

#pedir semilla
x=int(input("escriba un numero entero de 4 digitos: "))
m=int(input("numero de iteraciones: "))#numero de iteraciones
resultados=[]#creacion de lista para tabular
n=1#para bucle

while n<m+1:#el bucle se repetira el numero de iteraciones
  num=str(x)#convertir semilla a cadena
  if len(num)==4:#la semilla debe tener 4 digitos
    x1=x**2#se eleva al cuadrado
    num1=str(x1)#se cinvierte a cadena
    numero=list(num1)#se convierte en lista

    if len(numero)==8:#el nuevo numero debe tener 8 digitos
      xlist=numero[2:6]#extraer los numero medios
      numfin=int("".join(xlist))#pasar a numero entero

      #almacenar resultados en una lista, para la tabla
      resultados.append([n,x,x1,numfin])
      x=numfin#ahora el numero medio va a pasar a tomar el lugar de la semilla
      n=n+1#para que el bucle tenga fin
    else:
      xlist=numero[1:5]#en caso de tener menos de 8 digitos se toma un intervalo diferente de numeros
      numfin=int("".join(xlist))#pasar a numero, ya que era cadena

      #almacenar resultados en una lista, para la tabla
      resultados.append([n,x,x1,numfin])

      x=numfin#el numero toma el lugar de la semilla
      n=n+1#para que el bucle tenga fin

  else:
    print("el numero ingresado no tiene los digitos solicitados")
    n=10

#para imprimir tabla
tabla=["N","Xn","Digito al cuadrado","producto medio"]
print(tabulate.tabulate(resultados, headers=tabla, tablefmt="grid"))