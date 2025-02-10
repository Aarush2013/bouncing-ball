import pygame
import sys
pygame.init()
screen_width = 1290
screen_height = 737
circx,circy=645,368.5
circ_x,circ_y=645,368.5
radius=15
speed_x,speed_y=2,2
speedy_x,speedy_y=1,1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("bouncing ball")
background_color = ('black')

running = True
while running:

    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    circx += speed_x
    circy += speed_y

    if circx + radius > screen_width or circx - radius < 0:
        speed_x = - speed_x

    if circy + radius > screen_height or circy - radius < 0:
        speed_y = - speed_y

    circ_x += speedy_x
    circ_y += speedy_y

    if circ_x + radius > screen_width or circ_x - radius < 0:
        speedy_x = - speedy_x

    if circ_y + radius > screen_height or circ_y - radius < 0:
        speedy_y = - speedy_y

    pygame.draw.circle(screen,'blue',((circx),(circy)),radius)
    pygame.draw.circle(screen,'yellow',((circ_x),(circ_y)),radius)
    pygame.display.flip()
