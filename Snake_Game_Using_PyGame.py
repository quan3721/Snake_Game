# --- Create a game about Snake Using Pygame Library --- #

# -- Import Library -- #
import pygame
import random

# -- Initialize game -- #
pygame.init()

# -- Create a Game window -- #
window_width = 800 # -- width of window
window_height = 600 # -- height of window
window = pygame.display.set_mode(size=(window_width, window_height)) # -- create window
pygame.display.set_caption(title="Snake Game") # -- create caption for window

# -- Create color for snake -- #
white = (255, 255, 255) # -- White color

# -- Create color for window -- #
black = (0, 0, 0)

# -- Create color for food item -- #
red = (255, 0, 0)

# -- The initial dynamic position of Snake -- # ( Vị trí cố định ban đầu )
x1 = window_width / 2 # -- 400
y1 = window_height / 2 # -- 300
x1_change = 0
y1_change = 0

# -- Create initial length of Snake -- #
length_of_snake = 1

# -- Create initial list contain the block of body of Snake -- #
snake_body = []

# -- Create initial Score for game -- #
score = 0

# -- Random initial position of Food item -- #
food_x = round(random.randrange(0, window_width - 10) / 10) * 10.0 # round () : làm tròn, random.randrange(0, window_width - 10) : random từ 0 --> 800 - 10
food_y = round(random.randrange(0, window_height - 10) / 10) * 10.0

# -- Create a variable assigned class Clock of library Pygame to contain the function for controlling Frame Rate -- #
clock = pygame.time.Clock()

# -- Create a loop to show the window -- #
game_over = False
while not game_over: # not game_over = True
    for event in pygame.event.get(): # -- get the value of event from the window
        if event.type == pygame.QUIT: # -- Check the value event is equal the button 'x' click on window
            game_over = True # -- convert the value of game_over into True

        # -- check for arrow keys pressed -- # ( Kiểm tra các phím mũi tiên đã nhấn )
        if event.type == pygame.KEYDOWN: # -- Check the button pressed

            if event.key == pygame.K_LEFT: # -- Check the button arrow Key Left ( Kiểm tra phím mũi tên trái )
                x1_change = -10 # move left by 10 px, its means x1 - 10
                y1_change = 0

            elif event.key == pygame.K_RIGHT: # -- Check the button arrow Key Right ( Kiểm tra phím mũi tên phải )
                x1_change = 10 # move right by 10 px, its means x1 + 10
                y1_change = 0

            elif event.key == pygame.K_UP: # -- Check the button arrow Key Up ( Kiểm tra phím mũi tên lên )
                x1_change = 0
                y1_change = -10 # move up by 10 px, its means y1 - 10

            elif event.key == pygame.K_DOWN: # -- Check the button arrow Key Down ( Kiểm tra phím mũi tên xuống )
                x1_change = 0
                y1_change = 10 # move up by 10 px, its means y1 + 10

    # -- Update value for snake -- #
    x1 = x1 + x1_change
    y1 = y1 + y1_change

    # -- Quit Game when Snake move to boundaries of the window -- # ( Kết thúc game mỗi khi snake di chuyển ra ngoài khung hình của Game )
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0: # -- Check the position of snake are going out size of the window
        game_over = True # -- The game Quit

    window.fill(black) # -- fill black color for window after moving Snake

    # -- Add the position of Snake move into the list -- #
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    # -- Update the position of body snake -- #
    snake_body.append(snake_head) # -- append list snake_head into snake_body

    # -- Check the length of snake body with length of snake -- # ( When eat a food item, the block in snake body will have more 1 block, its means add more 1 position in snake_body )
    if len(snake_body) > length_of_snake: # If length of snake body is greater than length of snake, we will delete element index 0
        del snake_body[0]

    # -- Quit the game when Snake hitting itself -- #
    for segment in snake_body:
        if segment[-1] == snake_head:
            game_over = True

    # -- Display Score -- #
    font_style = pygame.font.SysFont(None, 30) # set font of Score Text
    score_text = font_style.render("Score: "+str(score), True, white)
    window.blit(score_text, (10, 10)) # Display score text with the postion

    # -- Random Food Item position when Snake move to eat the last Food Item  -- #
    if x1 == food_x and y1 == food_y: # -- check the position of Snake is equal food item position
        food_x = round(random.randrange(0, window_width - 10) / 10) * 10.0  # round () : làm tròn, random.randrange(0, window_width - 10) : random từ 0 --> 800 - 10
        food_y = round(random.randrange(0, window_height - 10) / 10) * 10.0
        length_of_snake += 1 # -- update the length of Snake when eating Food item
        score += 1 # -- update score

    # -- Add food Item for Snake Game -- #
    pygame.draw.rect(surface=window, color=red, rect=[food_x, food_y, 10, 10])

    # -- Create a shape for snake -- #
    # pygame.draw.rect(surface=window, color=white, rect=[400, 300, 10, 10]) # Create rectangle
    '''
        [400, 300, 10, 10] = [x, y, w, h]
        400, 300 : the position of snake based on width and height of window
        10, 10 : the size of snake ( width and height )
    '''
    # pygame.draw.rect(surface=window, color=white, rect=[x1, y1, 10, 10]) # Create rectangle
    for segment in snake_body:
        pygame.draw.rect(surface=window, color=white, rect=[segment[0], segment[1], 10, 10])  # Create rectangle
    pygame.display.update() # -- update into window when adding new something

    print(snake_head)
    print(snake_body)

    # -- Control Frame Rate -- #
    clock.tick(20) # -- set 20 FPS
