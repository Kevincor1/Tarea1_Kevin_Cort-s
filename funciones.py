#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np


# In[102]:


def Factorial(n): # funcion Factorial
    resultado = 1
    i = 1  
    while i <= n: #aca esta implicito la definicion: 0!=1
        resultado = resultado * i # multilplicacion recursiva
        i = i + 1
    return resultado

def Binomial(n,k): #funcion binomial
    return int(Factorial(n)/(Factorial(k)*Factorial(n-k))) #definimos los coef. binom. apartir de la funcion Factorial

def Prob(n,k): #Probabilidad de que al lanzar n veces una monededa, caiga k veces sello. (no es necesario, pero esta seria la funcion Prob.)
    return Binomial(n,k)/2.**n
        


# In[ ]:





# In[ ]:




