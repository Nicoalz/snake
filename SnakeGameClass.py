import pygame
import random

class Snake:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.size = 15
        self.length = 0
        self.list = []
        self.color = (0, 255, 0)
        self.speed = 3

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed
        snakeHead = []
        snakeHead.append(self.x)
        snakeHead.append(self.y)
        self.list.append(snakeHead)
        if len(self.list) > self.length:
            del self.list[0]

    def draw(self, screen):
        for i in self.list:
            pygame.draw.rect(screen, self.color,
                             (i[0], i[1], self.size, self.size))

    def isCollision(self, screenWidth, screenHeight):
        snakeHead = []
        snakeHead.append(self.x)
        snakeHead.append(self.y)
        if self.x < 0 or self.x > screenWidth or self.y < 0 or self.y > screenHeight or snakeHead in self.list[:-1]:
            return True
        return False

    def getPosition(self):
        return self.x, self.y

    def levelUp(self):
        self.speed += 0.1
        self.length += 1

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 10
        self.color = (255, 0, 0)

    def changePosition(self, screenWidth, screenHeight):
        self.x = random.randrange(50, screenWidth - 50)
        self.y = random.randrange(50, screenHeight - 50)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size, self.size))

    def isFoodEaten(self, snake):
        snakeRect = pygame.Rect(snake.getPosition()[0], snake.getPosition()[
                                1], snake.size, snake.size)
        foodRect = pygame.Rect(self.x, self.y, self.size, self.size)
        if snakeRect.colliderect(foodRect):
            return True
        return False