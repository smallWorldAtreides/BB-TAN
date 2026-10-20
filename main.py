import pygame
import random

pygame.init()

screen = pygame.display.set_mode((720, 1280))
clock = pygame.time.Clock()
running = True
rowMatrix = []
rowCounter = 0

blocksPerRow = 5 
blockWidth = screen.get_width() / blocksPerRow
blockSize = blockWidth - 10

def createRow():
    row = []
    for colIndex in range(blocksPerRow):
        zahl = random.randint(0,1)
        row.append(zahl)
    return row
"""""
for i in range(3):
    zahl = random.randint(0,1)
    row.append(zahl)
rowMatrix.append(row)
print(rowMatrix)

for rowIndex in range(3):
    row = []
    for colIndex in range(5):
        zahl = random.randint(0,1)
        row.append(zahl)
    rowMatrix.append(row)
"""
rowMatrix = [createRow()]
print(rowMatrix)

playerPos = pygame.Vector2(screen.get_width() / 2, 1280)

while running:    
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for rowIndex in range(len(rowMatrix)):
        for i in range(len(rowMatrix[rowIndex])):
            if rowMatrix[rowIndex][i] == 1:
                x = i * blockWidth + 5
                y = rowIndex * blockWidth + 5
                pygame.draw.rect(screen, 'white', (x, y, blockSize, blockSize))

    player = pygame.draw.circle(screen, 'white', playerPos, 30)
    
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
