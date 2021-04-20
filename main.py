import pygame
from pygame.locals import *

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((110,110,5))
    block = pygame.image.load("resources/block.png").convert()
    block = pygame.transform.scale(block, (20, 20))
    pygame.display.set_caption("Snake Game")
    block_x = 0
    block_y = 0
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event_key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False


