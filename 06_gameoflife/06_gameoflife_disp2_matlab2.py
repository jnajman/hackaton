import numpy
import matplotlib.pyplot as plt

# init test data
grid=numpy.zeros((10,10),int)
grid[0][2]=1    #glider
grid[1][3]=1
grid[2][1]=1
grid[2][2]=1
grid[2][3]=1

f = plt.figure()
ax = f.gca()
f.show()

for i in range(30):
    grid[0][0] += 1
    plt.imshow(grid,interpolation='none')
    f.canvas.draw()
    input('pauza')
