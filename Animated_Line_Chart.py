import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    x_val = float(input(f"Enter x[{i+1}]: "))
    y_val = float(input(f"Enter y[{i+1}]: "))
    x.append(x_val)
    y.append(y_val)

fig, ax = plt.subplots()
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_title("Animated Line Chart")

line, = ax.plot([], [], marker='o')

def update(frame):
    line.set_data(x[:frame+1], y[:frame+1])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=500, repeat=False)

plt.show()