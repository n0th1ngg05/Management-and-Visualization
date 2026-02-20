import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]
colors = ['skyblue', 'orange', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)  

plt.figure(figsize=(6, 6))
plt.pie(sizes, 
        labels=labels, 
        colors=colors, 
        explode=explode, 
        autopct='%1.1f%%', 
        shadow=True, 
        startangle=90)

plt.title('Programming Language Usage Distribution')

plt.axis('equal')

plt.show()
