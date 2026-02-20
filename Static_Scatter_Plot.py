import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
marks_scored = [35, 40, 50, 55, 65, 70, 80, 90]

plt.figure(figsize=(8, 5))
plt.scatter(hours_studied, marks_scored, 
            color='blue', 
            marker='o', 
            s=100)

plt.title('Scatter Plot: Hours Studied vs Marks Scored')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Scored')

plt.grid(True)

plt.show()
