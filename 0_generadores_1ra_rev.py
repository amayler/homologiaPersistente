######################################
# Importamos las bibliotecas necesarias
import numpy as np 
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
######################################

######################################
# Fijamos una semilla para que los resultados sean reproducibles
np.random.seed(0)
######################################

######################################
# Generamos 100 puntos aleatorios en el plano, cuyas
# coordenadas en X y Y varían en el rango 1-1000
# Estos puntos los guardamos en la variable `data1'
data1=np.random.randint(1,1000,(100,2))

# Generamos 100 puntos aleatorios en el plano, cuyas
# coordenadas en X y Y varían en el rango 2000-3000
# Estos puntos los guardamos en la variable `data2'
data2=np.random.randint(2000,3000,(100,2))

# Finalmente, con data1 y data2 formamos el conjunto de 
# puntos `data', al cual le aplicaremos las técnicas 
# de homología persistente 

data=np.vstack((data1,data2))
######################################

######################################
# Graficamos los puntos del conjunto `data'
x,y=data.T
plt.plot(x,y,'ro')
plt.show()
######################################

######################################
# Pedimos a Ripser que haga el diagrama de persistencia
# asociado a los puntos almacenados en `data'
diagrams=ripser(data)['dgms']
plot_diagrams(diagrams,show=True)
######################################