import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Gamme")
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("Gamme", False, "forestgreen")

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_x_pos = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,250))
        snail_x_pos -= 5
        if snail_x_pos < -40:
            snail_x_pos = 800
        screen.blit(snail_surface, (snail_x_pos, 220))

        screen.blit(text_surface, (340,75))
    pygame.display.update()
    clock.tick(30)