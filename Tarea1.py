#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from funciones import * #LLamamos todas las funciones de nuestro modulo


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




