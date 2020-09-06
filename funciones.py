#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np


# In[102]:


def Factorial(n): # funcion Factorial
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return resultado

def Binomial(n,k): #funcion binomial
    return int(Factorial(n)/(Factorial(k)*Factorial(n-k)))

def Prob(n,k): #Probabilidad de que al lanzar n veces una monededa, caiga k veces sello.
    return Binomial(n,k)/2.**n
        


# In[ ]:


#Triangulo de Pascal
def pascal(n): # definir la funcion
    archivo2 = open("Pascal-"+str(n)+".txt", "w+")  #nombres del archivo de texto y su variable asignada (el nombre del archivo de texto depende de n)
    for i in np.arange(0,n): #como dice en ña tarea un triangulo de n filas, desde n=0 hasta n-1
        Lista=[] # definimos una lista que nos permite crear el triangulo. En esta vamos a almacenar cada coeficiente binomial de cada fila.
        for k in np.arange(i+1):
            Lista.append(Binomial(i,k)) #usamos la funcion Binomial de nuestro modulo
        c=str(Lista) #convertimos nuestra lista en un string asignado a la variable c
        c = c.replace(',', '') # elimina las comas de c
        c= c.replace('[','') 
        c=c.replace(']','') # esta y la anterior linea borran las llaves de c
        b=[]   
        for l in np.arange(len(c)):  #Este for es para darle forma a la piramide usando los algoritmos que vimos en la clase
            if c[l]==" ":
                b.append(c[l]+((4)*" "))
            else:
                b.append(c[l])
        archivo2.write("n=" + str(i))
        archivo2.write(((2*(n+9-i)-i-4*int((i)/10.))*" "))
        for m in b:
            archivo2.write(m)
        archivo2.write("\n") 
        archivo2.write("\n") # un espacio entre lineas
         
    archivo2.close() # cerramos el archivo


# In[ ]:




