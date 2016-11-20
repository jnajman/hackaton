import pygame, sys, time
pygame.init() # initialize the pygame system
size = (500, 500) # window size is a 2-tuple measured in px
screen = pygame.display.set_mode(size)
margin=10

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the clock
clock = pygame.time.Clock()
max_fps = 60 # maximum number of cycles (frames) per second

while True:
    clock.tick(max_fps)  # limit the refresh rate to a max of 60 cycles per second

    # Quit when the user closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position whenever it moves
            mouse_position = event.pos  # event.pos is a mouse position 2-tuple
            print(mouse_position)


    screen.fill((255, 255, 255))  # RGB white color tuple

    # screen.blit(tile, (200, 100))  # Draw the tile on the screen

    pygame.display.flip()  # Display what was drawn this turn