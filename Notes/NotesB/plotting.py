# plotting (with matplotlib)
import matplotlib.pyplot as plt

plt.figure(1)  # creates a new plot

plt.plot([1, 2, 3, 4, 0])  # plots the items in the list plots x against y

plt.plot([1, 2, 3, 4], [12, 8, 2, 1])  # ([x points], [y points])


plt.figure(2)

xpoints = [x for x in range(1, 11)]
ypoints = [y ** 2 for y in xpoints]

plt.plot(xpoints, ypoints, color='purple', marker='*', markersize=10, linestyle='--', alpha=0.5, linewidth=4)


# TALUNK title, axes, labels, units, numbers, key

plt.title("Amount of onion")
plt.xlabel("AHH TOO MANY ONION", color='green', fontsize=15)
plt.ylabel("Onion", color='green', fontsize=15)
plt.axis([0, 11, 0, 110])


plt.show()










