import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"Score: {score}", False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time

def title_text():
    title_game = test_font2.render(f"Gamme", False, (255,255,255))
    title_game_rectangle = title_game.get_rect(midbottom = player_stand_rectangle.midtop)
    screen.blit(title_game, title_game_rectangle)
    title_score = test_font3.render(f"Score: {score}",False, (255,255,255))
    title_score_rectangle = title_score.get_rect(midtop = player_stand_rectangle.midbottom)
    if score != 0:
        screen.blit(title_score,title_score_rectangle)
    title_words = test_font.render(f"Press 'SPACE' to restart",False, (255,255,255))
    title_words_rectangle = title_words.get_rect(midtop = title_score_rectangle.midbottom)
    screen.blit(title_words,title_words_rectangle)

pygame.init()

game_active = False

score = 0

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Gamme")
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
test_font2 = pygame.font.Font("font/Pixeltype.ttf", 100)
test_font3 = pygame.font.Font("font/Pixeltype.ttf", 70)

start_time = 0

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# score_surface = test_font.render("Current Score: ", False, (64,64,64))
# score_rectangle = score_surface.get_rect(center =(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

#death screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos):
                        player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
        # if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_SPACE:
    
    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rectangle)
        # screen.blit(score_surface, score_rectangle)
        score = display_score()

        #snail
        snail_rectangle.left -= 5
        if snail_rectangle.right < 0: snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        #player
        player_gravity += 1
        player_rectangle.y  += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)

        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rectangle)

        title_text()

    pygame.display.update()
    clock.tick(60)
