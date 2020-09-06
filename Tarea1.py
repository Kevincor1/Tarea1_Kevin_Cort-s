#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from funciones import * #LLamamos todas las funciones de nuestro modulo


# In[30]:


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


# In[65]:


#Probabilidad de la moneda:
#punto 4.a
print("La probabilidad de obtener 10 caras, si se hace 100 veces el exp. es: " , Binomial(100,10)/2.**100)

#punto 4.b
#debemos considerar todos los eventos en los que cayo mas de 30 veces.
suma=0
for i in np.arange(31,101): # sumamos sobre todos los k en la formula dada para la probab. desde 31 hasta 100
    suma=suma+Binomial(100,i)/2.**100
print("La probabilidad de obtener mas de 30 caras si se hace 100 veces es:", suma)



# In[57]:





# In[ ]:





# In[ ]:




