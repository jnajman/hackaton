import numpy
import matplotlib.pyplot as plt

# init test data
# grid=numpy.zeros((10,10),int)
# grid[0][2]=1    #glider
# grid[1][3]=1
# grid[2][1]=1
# grid[2][2]=1
# grid[2][3]=1

f = plt.figure()
ax = f.gca()
f.show()

# for i in range(30):
#     grid[0][0] += 1
#     plt.imshow(grid,interpolation='none')
#     f.canvas.draw()



    #-------------------------------------------------------------------------
width=100
height=100
# grid = [[0 for x in range(width)] for y in range(height)]
grid=numpy.zeros((width,height),int)

# #glider:
grid[0][2]=1
grid[1][3]=1
grid[2][1]=1
grid[2][2]=1
grid[2][3]=1

#oscilator:
# grid[2][1]=1
# grid[2][2]=1
# grid[2][3]=1

for step in range(100):#kroky simulace

    # for i in range(len(grid)): #vypise matici
    #     print(grid[i])
    plt.cla()
    plt.imshow(grid, cmap=plt.get_cmap('viridis'), interpolation='none') #vykresli matici
    f.canvas.draw()

    # input('pauza')      #---PAUZA---

    grid_new = numpy.zeros((width, height), int)  # nova matice (na zacatku vynulovana)

    for m in range(height):#po radcich
        for n in range(width):#po sloupcich
            num_of_neighbours=0 #vynulovat pred kazdou novou bunkou
            #
            #operace pro danou bunku:
            #

            try:#podivej nahoru
                if grid[m-1][n]==1:
                    num_of_neighbours+=1
            except IndexError:
                pass

            try:  # podivej vpravo nahoru
                if grid[m - 1][n+1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej vpravo
                if grid[m][n+1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej vpravo dolu
                if grid[m+1][n+1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej dolu
                if grid[m + 1][n] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej vlevo dolu
                if grid[m + 1][n - 1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej vlevo
                if grid[m][n-1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            try:  # podivej vlevo nahoru
                if grid[m - 1][n - 1] == 1:
                    num_of_neighbours += 1
            except IndexError:
                pass

            if grid[m][n]==0:               #pokud je aktualni bunka mrtva...
                if num_of_neighbours==3:    #...ale ma 3 sousedy...
                    grid_new[m][n]=1        #... --> ozivit (jinak je defaultne mrtva)

            if grid[m][n]==1:                                       #pokud je aktualni bunka ziva...
                if num_of_neighbours==2 or num_of_neighbours==3:    #...a ma 2 nebo 3 sousedy...
                    grid_new[m][n] = 1                              #...nech ji zit (jinak je defaultne mrtva)

    grid=numpy.copy(grid_new) #update zakladni grid