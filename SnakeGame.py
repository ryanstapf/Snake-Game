import pygame
import time
import random

# Dictates the frame rate of the application
snake_speed = 15

# Window size
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize the pygame module
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Snake default position
snake_position = [100, 50]

# First four blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Set initial snake color to green
snake_color = green

# Randomly place the fruit in the window
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Initialize the pause boolean to false
pause = False

# Initialize the party mode boolean to false
party = False

# Sets the initial direction of the snake to right
direction = 'RIGHT'
change_to = direction

# Initialize score to 0
score = 0


# Display Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)


# Game Over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:

    # Key press event handlers
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            # Press Q to quit the game
            if event.key == pygame.K_q:
                game_over()

            # Press P to pause the game
            if event.key == pygame.K_p:
                if pause == False:
                    pause = True
                else:
                    pause = False

            # Press C to randomly change snake color
            if event.key == pygame.K_c:
                r_val = random.randrange(255)
                g_val = random.randrange(255)
                b_val = random.randrange(255)
                snake_color = (r_val, g_val, b_val)

            # Press R to initialize party mode
            if event.key == pygame.K_r:
                if party == False:
                    party = True
                else:
                    party = False


    # Party mode
    if party == True:
        r_val = random.randrange(255)
        g_val = random.randrange(255)
        b_val = random.randrange(255)
        snake_color = (r_val, g_val, b_val)


    # If two keys pressed simultaneously to prevent the snake from moving in two directions at once
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


    # Moves the snake if the pause boolean is False (i.e. game is not paused)
    if direction == 'UP' and pause == False:
        snake_position[1] -= 10
    else:
        snake_position[1] -= 0

    if direction == 'DOWN' and pause == False:
        snake_position[1] += 10
    else:
        snake_position[1] += 0
        
    if direction == 'LEFT' and pause == False:
        snake_position[0] -= 10
    else:
        snake_position[0] -= 0
        
    if direction == 'RIGHT' and pause == False:
        snake_position[0] += 10
    else:
        snake_position[0] += 0
        

    # Snake body growing mechanism
    # If fruits and snakes collide then score will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, snake_color,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))


    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1] and pause == False:
            game_over()
            

    # Displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second
    fps.tick(snake_speed)