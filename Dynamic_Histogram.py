import numpy as np
import matplotlib.pyplot as mpl

n = int(input("Enter array list: "))
histdata = []
for i in range(n):
    histdata.append(int(input("Enter value: ")))
    
mpl.hist(histdata)
mpl.show()