import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Create figure and axis
fig, ax = plt.subplots()

x_data = []
y_data = []

def update(frame):
    # Add new random data points
    x_data.append(random.randint(0, 50))
    y_data.append(random.randint(0, 100))
    
    ax.clear()  # Clear previous frame
    ax.scatter(x_data, y_data, color='red')
    
    ax.set_title("Dynamic Scatter Plot")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    ax.grid(True)

# Animate (updates every 1 second)
ani = FuncAnimation(fig, update, interval=1000)

plt.show()
