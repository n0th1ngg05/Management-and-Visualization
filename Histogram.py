import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))

data = []

for i in range(n):
    value = float(input(f"Enter value[{i+1}]: "))
    data.append(value)

bins = int(input("Enter number of bins: "))

plt.hist(data, bins=bins, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()