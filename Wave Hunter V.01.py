import pygame
pygame.init()
screen_width = 640
screen_height = 360


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wave Hunter")


player_position = [320, 180]
player_size = 128
player_velocity = 5

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position[0] -= player_velocity
    if keys[pygame.K_RIGHT]:
        player_position[0] += player_velocity
        
    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen, (255, 0, 0), (player_position[0], player_position[1], player_size, player_size))
    pygame.display.flip()  

pygame.quit()
