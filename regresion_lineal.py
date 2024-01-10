
import numpy as np
import matplotlib.pyplot as plt

x = np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array ([1, 2.5, 3, 3.5, 5, 6, 6.5, 8, 9.5])

coefs = np.polyfit (x, y, 1)
print (coefs)

m = coefs[0]            # la pendiente de la recta
b = coefs[1]            # La ordenada al origen  

y_est = m * x + b       # Obtiene la y correspondiente a la x
plt.plot (x, y_est)     # Pinta el punto
plt.scatter (x, y) 
plt.show ()
