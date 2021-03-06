import numpy

width=5
height=5
# grid = [[0 for x in range(width)] for y in range(height)]
grid=numpy.zeros((width,height),int)

# print(len(grid))

grid[0][2]=1
grid[1][3]=1
grid[2][1]=1
grid[2][2]=1
grid[2][3]=1

# grid=numpy.zeros((5,5),int)
# print(grid[1][1])

# grid2=numpy.copy(grid)
# grid3=numpy.copy(grid)
#
# grid2[4][4]=5
#
# grid=numpy.copy(grid2)

# for i in range(len(grid)):
#     print(grid[i])

# num_of_neighbours <2 --> DIE
# num_of_neighbours >3 --> DIE
# num_of_neighbours 2 or 3 --> LIVE
# num_of_neighbours == 3 --> RESSURECT (if dead)

# input('pauza')
#
for step in range(10):#kroky simulace

    for i in range(len(grid)): #vykresli matici
        print(grid[i])

    input('pauza')      #---PAUZA---

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


# try:
#     grid[100]
# except IndexError:
#     print('au')