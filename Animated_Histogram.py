import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(input("Enter number of values: "))

data = []

for i in range(n):
    value = float(input(f"Enter value[{i+1}]: "))
    data.append(value)

bins = int(input("Enter number of bins: "))

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.hist(data[:frame+1], bins=bins, edgecolor='black')
    ax.set_title("Animated Histogram")

ani = animation.FuncAnimation(fig, update, frames=len(data), interval=500, repeat=False)

plt.show()