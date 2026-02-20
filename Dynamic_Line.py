import numpy as np
import matplotlib.pyplot as mpl

n = int(input("Enter number of elements: "))

x_values = []
y_values = []

for i in range(n):
    x = float(input("Enter x values: "))
    y = float(input("Enter y values: "))
    
    x_values.append(x)
    y_values.append(y)

x_arr = np.array(x_values)
y_arr = np.array(y_values)

mpl.plot(x_arr, y_arr)
mpl.show()