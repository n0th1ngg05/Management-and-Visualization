import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)

xdata, ydata = [], []
line, =  ax.plot([], [])

def animate(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame) + 5)
    line.set_data(xdata, ydata)
    return line, 

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 50), interval = 100)

plt.show()