import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

labels = ['Python', 'Java', 'C++', 'JavaScript']

def generate_data():
    return [random.randint(10, 50) for _ in range(4)]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()  
    data = generate_data()
    ax.pie(data,
           labels=labels,
           autopct='%1.1f%%',
           startangle=90)
    ax.set_title('Dynamic Programming Language Usage')

ani = FuncAnimation(fig, update, interval=1000)

plt.show()
