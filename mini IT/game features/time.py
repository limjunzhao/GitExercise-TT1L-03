import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 24)
clock_font = pygame.font.SysFont(None, 36)
time_up_font = pygame.font.SysFont(None, 72)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")

def format_time(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds %= 60
    return "{:02d}:{:02d}".format(minutes, seconds)

def display_time_up():
    time_up_surface = time_up_font.render("Time's Up!", True, WHITE)
    time_up_rect = time_up_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(time_up_surface, time_up_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds
    pygame.quit()
    sys.exit()

start_time = pygame.time.get_ticks()
time_up = False

while True:
    screen.fill(BLACK) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    formatted_time = format_time(elapsed_time)

    if elapsed_time >= 10000 and not time_up:
        time_up = True
        display_time_up()

    clock_surface = clock_font.render(formatted_time, True, WHITE)
    clock_rect = clock_surface.get_rect(topright=(screen_width - 10, 10))
    screen.blit(clock_surface, clock_rect)

    pygame.display.flip()
    clock.tick(60)
