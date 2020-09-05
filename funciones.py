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





# In[ ]:




