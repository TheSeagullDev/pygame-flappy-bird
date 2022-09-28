import pygame
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

X_VEL = 3

EVENT_CREATE_PIPES = pygame.USEREVENT + 1

def draw_window(bird, top_pipe, bottom_pipe):
    WIN.fill((255, 255, 255))
    for pipe in top_pipe:
        pygame.draw.rect(WIN, (0, 255, 0), pipe)
    for pipe in bottom_pipe:
        pygame.draw.rect(WIN, (0, 255, 0), pipe)
    pygame.draw.rect(WIN, (255, 0, 0), bird)
    pygame.display.update()

def handle_gravity(bird, y_vel):
    if bird.y - y_vel < HEIGHT - 40:
        y_vel -= 0.5
        bird.y -= y_vel
        print(y_vel)
    return y_vel

def handle_pipes(top_pipe, bottom_pipe):
    for pipe in top_pipe:
        pipe.x -= X_VEL
    for pipe in bottom_pipe:
        pipe.x -= X_VEL

def main():
    bird = pygame.Rect(200, 200, 40, 40)
    top_pipe = []
    bottom_pipe = []
    y_vel = 0
    run = True
    clock = pygame.time.Clock()
    pygame.time.set_timer(EVENT_CREATE_PIPES, 2000)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_vel = 10 
            if event.type == EVENT_CREATE_PIPES:
                pipe_offset = random.randint(-300, 0)
                top_pipe.append(pygame.Rect(WIDTH, 0 + pipe_offset, 75, 325))
                bottom_pipe.append(pygame.Rect(WIDTH, HEIGHT + pipe_offset, 75, 325))
                print(pipe_offset)

        y_vel = handle_gravity(bird, y_vel)
        handle_pipes(top_pipe, bottom_pipe)
        draw_window(bird, top_pipe, bottom_pipe)

    pygame.quit()


if __name__ == '__main__':
    main()