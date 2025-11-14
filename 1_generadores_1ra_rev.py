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
# Generamos un conjunto aleatorio `data'
x1=np.random.randint(1,100,(100,1))
y1=np.random.randint(100,200,(100,1))
data1=np.vstack((x1.T,y1.T)).T 

x2=np.random.randint(100,200,(100,1))
y2=np.random.randint(200,300,(100,1))
data2=np.vstack((x2.T,y2.T)).T

x3=np.random.randint(200,300,(100,1))
y3=np.random.randint(100,200,(100,1))
data3=np.vstack((x3.T,y3.T)).T

x4=np.random.randint(100,200,(100,1))
y4=np.random.randint(1,100,(100,1))
data4=np.vstack((x4.T,y4.T)).T

data_uno=np.vstack((data1,data2)).T
data_dos=np.vstack((data3,data4)).T
data=np.vstack((data_uno.T,data_dos.T))
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