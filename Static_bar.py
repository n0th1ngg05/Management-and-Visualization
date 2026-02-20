import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

categories = ['A', 'B', 'C', 'D']
values = [5, 6, 7, 8]

plt.figure()
plt.bar(categories, values)
plt.title("Static Bar Chart")
plt.show()