import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
    
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def  update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == "fly":
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
    
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
            if self.rect.x <= -100:
                self.kill

    def update(self):
        self.animation_state()
        self.rect.x -= obstacle_speed
        self.destroy
    
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"Score: {score}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def title_text():
    title_game = test_font2.render(f"Gamme", False, (255,255,255))
    title_game_rect = title_game.get_rect(midbottom = player_stand_rect.midtop)
    screen.blit(title_game, title_game_rect)
    title_score = test_font3.render(f"Score: {score}",False, (255,255,255))
    title_score_rect = title_score.get_rect(midtop = player_stand_rect.midbottom)
    title_words = test_font.render(f"Press 'SPACE' to play",False, (255,255,255))
    title_words_rect = title_words.get_rect(midtop = title_score_rect.midbottom)
    
    if score != 0: screen.blit(title_score,title_score_rect)
    else: screen.blit(title_words,title_words_rect)
obstacle_speed = 5

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= obstacle_speed 

            if obstacle_rect.bottom == 300: screen.blit(snail_surface,obstacle_rect)
            else:screen.blit(fly_surface,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def collsion_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]
pygame.init()
game_active = False
score = 0

bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.2)
bg_music.play(loops= -1)

screen = pygame.display.set_mode((800,400))

pygame.display.set_caption("Gamme")
clock = pygame.time.Clock()


test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
test_font2 = pygame.font.Font("font/Pixeltype.ttf", 100)
test_font3 = pygame.font.Font("font/Pixeltype.ttf", 70)

start_time = 0

# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
 
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# score_surface = test_font.render("Current Score: ", False, (64,64,64))
# score_rect = score_surface.get_rect(center =(400, 50))

# snail
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]
# fly
fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

#death screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 400)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                        player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        # if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_SPACE:
        if game_active:    
            if event.type == obstacle_timer and game_active:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail",])))
                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100), 180)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # screen.blit(score_surface, score_rect)
        score = display_score()
        
        
        #snail
        # snail_rect.left -= 5
        # if snail_rect.right < 0: snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        #player
        # player_gravity += 1
        # player_rect.y  += player_gravity

        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface,player_rect)
        
        player.draw(screen)
        player.update()

        obstacle_group.update()
        obstacle_group.draw(screen)
    
        # obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
        game_active = collsion_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
        obstacle_speed += 0.003

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        title_text()
        obstacle_rect_list.clear()
        player_rect.y = 300
        player_gravity = 0

        obstacle_speed = 5


    pygame.display.update()
    clock.tick(60)
