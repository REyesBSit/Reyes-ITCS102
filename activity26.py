import pygame
import random

def game():
    print("Explanation:")
    print("")
    end_prompt = input("To continue the game, Press Enter...")
    # Initialize Pygame
    pygame.init()

    # Game window dimensions
    window_x = 720
    window_y = 480

    # Define colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)

    # Set up the game window
    pygame.display.set_caption('Pygame Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS controller
    fps = pygame.time.Clock()

    # Snake properties
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_speed = 15

    # Food properties
    food_position = [random.randrange(1, (window_x // 10)) * 10,
                    random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True

    # Initial direction
    direction = 'RIGHT'
    change_to = direction

    # Score
    score = 0

    # Game over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score: ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'

        # Validate direction change
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawn new food
        if not food_spawn:
            food_position = [random.randrange(1, (window_x // 10)) * 10,
                            random.randrange(1, (window_y // 10)) * 10]
        food_spawn = True

        # Drawing the game elements
        game_window.fill(black)
        for block in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(block[0], block[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

        # Game over conditions
        # Out of bounds
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Self-collision
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Display score
        my_font = pygame.font.SysFont('times new roman', 20)
        score_surface = my_font.render('Score : ' + str(score), True, white)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

        # Refresh game screen
        pygame.display.update()

        # Control game speed
        fps.tick(snake_speed)