import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600
cell_size = 20
snake_block = 20


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / cell_size) * cell_size
    foody = round(random.randrange(0, dis_height - snake_block) / cell_size) * cell_size

    score = 0

    start_time = time.time()

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Ты проиграл! Нажми C для продолжения или Q для выхода", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -cell_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = cell_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -cell_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = cell_size
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(dis, black, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / cell_size) * cell_size
            foody = round(random.randrange(0, dis_height - snake_block) / cell_size) * cell_size
            length_of_snake += 1
            score += 10

        elapsed_time = time.time() - start_time
        time_str = "{:.2f}".format(elapsed_time)
        pygame.display.set_caption(f"Змейка на Pygame | Счёт: {score} Время: {time_str}")

        clock.tick(15)

    pygame.quit()
    quit()


gameLoop()
