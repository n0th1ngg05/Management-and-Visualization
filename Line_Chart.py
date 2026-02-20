import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    x_val = float(input(f"Enter x[{i+1}]: "))
    y_val = float(input(f"Enter y[{i+1}]: "))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y, marker='o')
plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

plt.show()