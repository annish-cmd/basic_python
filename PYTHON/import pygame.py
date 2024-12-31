import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food
snake_block = 20
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.dx = snake_block
        self.dy = 0
        self.body = []
        self.length = 1

    def move(self):
        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, [segment[0], segment[1], snake_block, snake_block])

# Food class
class Food:
    def __init__(self):
        self.x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    def draw(self):
        pygame.draw.rect(window, RED, [self.x, self.y, snake_block, snake_block])

    def respawn(self):
        self.x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

def game_loop():
    game_over = False
    snake = Snake()
    food = Food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx != snake_block:
                    snake.dx = -snake_block
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT and snake.dx != -snake_block:
                    snake.dx = snake_block
                    snake.dy = 0
                elif event.key == pygame.K_UP and snake.dy != snake_block:
                    snake.dx = 0
                    snake.dy = -snake_block
                elif event.key == pygame.K_DOWN and snake.dy != -snake_block:
                    snake.dx = 0
                    snake.dy = snake_block

        # Check for collision with walls
        if snake.x >= width or snake.x < 0 or snake.y >= height or snake.y < 0:
            game_over = True

        # Check for collision with self
        for segment in snake.body[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                game_over = True

        # Check for collision with food
        if snake.x == food.x and snake.y == food.y:
            food.respawn()
            snake.length += 1

        window.fill(BLACK)
        snake.move()
        snake.draw()
        food.draw()
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
