import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)

circle, = ax.plot([], [], marker = 'o', markersize = 15)

def animate(frame):
    circle.set_data([frame], [5])
    return circle, 

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 50), interval = 100)

plt.show()