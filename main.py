from ArrowTracker import ArrowTracker
import pygame
from stats import readfile, writefile

    
# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
col1 = [255,0,0]
col2 = [0,0,255]
col3 = [0,255,0] 

loadedSteps = readfile()

pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((300, 300))

kirby_ctrl = pygame.image.load('img/ctrlbase.png').convert_alpha()
kirby_bg = pygame.image.load('img/kirby-bg.png').convert_alpha()
kirby_a = pygame.image.load('img/ab-a.png').convert_alpha()
kirby_b = pygame.image.load('img/ab-b.png').convert_alpha()
kirby_ab_neut = pygame.image.load('img/ab-neutral.png').convert_alpha()
kirby_left = pygame.image.load('img/kirby-left.png').convert_alpha()
kirby_right = pygame.image.load('img/kirby-right.png').convert_alpha()
kirby_down = pygame.image.load('img/kirby-down.png').convert_alpha()
kirby_neut = pygame.image.load('img/kirby-neut.png').convert_alpha()

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()


pad = pygame.Rect(0,0,150,150)
left =  pygame.Rect(0, 50, 50, 50)
down =  pygame.Rect(50, 100, 50, 50)
up  =  pygame.Rect(50, 0, 50, 50)
right =  pygame.Rect(100, 50, 50, 50)

   
at = ArrowTracker()

# -------- Main Program Loop -----------
while not done:    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.        
    at.update()
    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    screen.blit(kirby_bg,(0,0))
    screen.blit(kirby_ctrl,(0,0))
    if at.down:
        screen.blit(kirby_down,(0,0))
    elif at.left:
        screen.blit(kirby_left,(0,0))
    elif at.right:
        screen.blit(kirby_right,(0,0))
    else:
        screen.blit(kirby_neut,(0,0))
    if at.a:
        screen.blit(kirby_a,(0,0))
    elif at.b:
        screen.blit(kirby_b,(0,0))
    else:
        screen.blit(kirby_ab_neut,(0,0))
    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #
    joystick_count = pygame.joystick.get_count()
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(60)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()