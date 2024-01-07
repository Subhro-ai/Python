import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time ) / 1000)
    score_surface = test_font.render(f'Score : {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()



snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (800,300))

player_surf = pygame.image.load('I:\Python\PyGame\graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

start_time = 0

player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 800
                start_time = pygame.time.get_ticks()
                
            
    if game_active:        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(text_surface, text_rect)
        display_score()
        screen.blit(snail_surface,snail_rect)
        if snail_rect.right < 0: snail_rect.right = 800
        snail_rect.right -= 4


        #player
        screen.blit(player_surf,player_rect)
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        if(player_rect.colliderect(snail_rect)):
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand ,player_stand_rect)
        

    pygame.display.update()
    clock.tick(60)
