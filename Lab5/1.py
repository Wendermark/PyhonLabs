import numpy as np

x = 1.5

y = (np.sin(np.pi/2 + 1)**2 + x * np.power(3 + x**2, 1/4) - np.tan(x**3 - 1)**3) / (np.arctan(x/2) - np.log(17.56))

print(y)