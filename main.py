import pygame


def draw(screen, x, y):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), [0, 0], [x, y], 5)
    pygame.draw.line(screen, (255, 255, 255), [0, y], [x, 0], 5)


a = input()
b = input()
try:
    a = int(a)
    b = int(b)
except ValueError:
    print('Неверный формат')
    a = None

if __name__ == '__main__' and a:
    pygame.init()
    size = width, height = a, b
    screen = pygame.display.set_mode(size)
    draw(screen, a, b)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
