import pygame
from sys import exit

pygame.init()

game_active = True

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Gamme")
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

player_score = 0
score_surface = test_font.render("Current Score: ", False, (64,64,64))
score_rectangle = score_surface.get_rect(center =(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos):
                    player_gravity = -20
            
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300 or event.key == pygame.K_UP and player_rectangle.bottom >= 300:
               player_gravity = -20
                   
        # if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_SPACE:
    
    if game_active:
        score_surface = test_font.render("Current Score: " + str(int(player_score)), False, (64,64,64))

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, "#c0e8ec", score_rectangle)
        
        screen.blit(score_surface, score_rectangle)

        #snail
        snail_rectangle.left -= 4
        if snail_rectangle.right < 0: snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        #player
        player_gravity += 1
        player_rectangle.y  += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)

        player_score += 1/120

        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        screen.fill("red")

    pygame.display.update()
    clock.tick(60)
