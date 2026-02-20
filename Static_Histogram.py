import numpy as np
import matplotlib.pyplot as mpl

data = np.array([10,15,100])
mpl.hist(data, bins=10, color="red")
mpl.xlabel("Values")
mpl.ylabel("Frequency")
mpl.title("Basic Histogram")
mpl.show()