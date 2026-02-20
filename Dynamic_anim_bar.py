import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n= int(input("Enter number of bars: "))

categories = []
values = []

for i in range(n):
    name = input(f"Enter laber for bar {i+1}: ")
    value = int(input(f"Enter value for {name}: "))
    
    categories.append(name)
    values.append(value)
    
plt.bar(categories, values)
plt.title("Dynamic bar chart")
plt.show()