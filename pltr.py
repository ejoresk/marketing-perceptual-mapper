import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from os import chdir


# navigate file structure
chdir("csv_files")
filename = input("file name:  ")

xr, yr, zr = [], [], []

# extract point values from csv
with open(filename, newline="") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	header = next(reader)
	if header != None:
		for i in reader:
			xr.append(float(i[1]))
			yr.append(float(i[2]))
			zr.append(float(i[3]))

data_raw, data_unique = [], []
# get list of unique plot points
for i in zip(xr, yr, zr):
	data_raw.append(i)
for i in data_raw:
	if i not in data_unique:
		data_unique.append(i)

point_frequency = []
# get frequency of unique points
for i in data_unique:
	c = 0
	for j in data_raw:
		if i == j:
			c += 1
	point_frequency.append(str(c))

xu, yu, zu = [], [], []
# split points by axes
for i in data_unique:
	xu.append(i[0])
	yu.append(i[1])
	zu.append(i[2])

# assign custom point marker weights
# n = len(data_raw)

# make scatterplot
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(xu, yu, zu, s=100)

for x, y, z, i in zip(xu, yu, zu, point_frequency):
	ax.text(x, y, z, i, size=15)

# set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# set axis ticks
ax.set_xticks(np.arange(-1, 1, step=.5))
ax.set_yticks(np.arange(-1, 1, step=.5))
ax.set_zticks(np.arange(-1, 1, step=.5))

# set title and axis names
ax.set_title(input("plot title:  "))
ax.set_xlabel(input("x axis:  "))
ax.set_ylabel(input("y axis:  "))
ax.set_zlabel(input("z axis:  "))

plt.show()

