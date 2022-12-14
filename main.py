import pygame
from SnakeGameClass import Snake, Food
import time
pygame.init()
snake = Snake()
food = Food()
screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Snake')
game_over = False
foodInit = True
xChange = 0
yChange = 0
clock = pygame.time.Clock()

def displatMessage(message, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(message, True, color)
    screen.blit(mesg, [screenWidth/2.5, screenHeight/2.5])

def displayScore(score):
    font_style = pygame.font.SysFont(None, 30)
    value = font_style.render(
        "Your Score: " + str(score), True, (255, 255, 255))
    screen.blit(value, [0, 0])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -1
                yChange = 0
            elif event.key == pygame.K_RIGHT:
                xChange = 1
                yChange = 0
            elif event.key == pygame.K_UP:
                xChange = 0
                yChange = -1
            elif event.key == pygame.K_DOWN:
                xChange = 0
                yChange = 1

    screen.fill((0, 0, 0))
    snake.move(xChange, yChange)
    snake.draw(screen)
    food.draw(screen)

    if food.isFoodEaten(snake) or foodInit:
        food.changePosition(screenWidth, screenHeight)
        foodInit = False
        snake.levelUp()

    displayScore(snake.length - 1)
    pygame.display.update()
    game_over = snake.isCollision(screenWidth, screenHeight)
    clock.tick(30)

displatMessage("You Lost", (255, 0, 0))
pygame.display.update()
time.sleep(2)
pygame.quit()