import matplotlib.pyplot as plt
from matplotlib import style
"""
Plotting the points :
    a(1,4) , b(2,5), c(3,6)
"""

# plt.plot([1, 2, 3],[4, 5, 6])
# plt.show()

"""
Ploting with adding more informations:
"""
# x = [5, 2, 8]
# y = [2, 6, 7]
# plt.plot(x, y)
# plt.title('MESSAGE')
# plt.ylabel('yAxis')
# plt.xlabel('xAxis')
# plt.show()

"""
Ploting with adding more informations and STYLE
"""

# style.use('ggplot')
# x = [5, 13, 8]
# y = [12, 1, 7]

# x1 = [6, 10, 5]
# x2 = [1, 9, 5]

# plt.plot(x, y, 'g', label = "line first", linewidth=4)
# plt.plot(x1, x2, 'r', label = "line second", linewidth=2)

# plt.title("Graph")
# plt.ylabel('yaxis')
# plt.xlabel('xaxis')
# plt.grid(True, color='k')

# plt.show()

"""
BAR GRAPH

"""

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50,40, 70, 80, 20], label="Male", width=0.5)

plt.legend()
plt.xlabel('Height')
plt.ylabel('age')
plt.title("Information")
plt.show()