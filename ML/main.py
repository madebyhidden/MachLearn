import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 640
screen_height = 480

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Змейка')

# Определение параметров змейки
block_size = 10
snake_speed = 15

# Определение шрифта
font = pygame.font.SysFont(None, 25)


# Определение функции вывода текста на экран
def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [screen_width / 6, screen_height / 3])


# Определение функции змейки
def snake(block_size, snakeList):
    for x in snakeList:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])


# Определение главной функции
def gameLoop():
    gameExit = False
    gameOver = False

    # Начальные координаты змейки
    lead_x = screen_width / 2
    lead_y = screen_height / 2

    # Начальное изменение координат змейки
    lead_x_change = 0
    lead_y_change = 0

    # Начальный список координат змейки
    snakeList = []
    snakeLength = 1

    # Определение начальной позиции еды
    randAppleX = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Основной игровой цикл
    while not gameExit:
        while gameOver == True:
            screen.fill(white)
            message("Вы проиграли. Нажмите C для продолжения или Q для выхода.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Обработка нажатий на клавиши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Обновление координат змейки
        lead_x += lead_x_change
        lead_y += lead_y_change
        # Проверка на столкновение со стенами
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            gameOver = True

        # Добавление новой головы змейки в список координат
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # Удаление лишних координат змейки
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Проверка на столкновение с телом змейки
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True



        # Обновление экрана
        pygame.display.update()

        # Проверка на съедание еды
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snakeLength += 1

        # Очистка экрана
        screen.fill(white)

        # Рисование змейки
        snake(block_size, snakeList)
        # Рисование еды
        pygame.draw.rect(screen, red, [randAppleX, randAppleY, block_size, block_size])

        # Обновление экрана
        pygame.display.update()

        # Задержка
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Выход из Pygame
    pygame.quit()


gameLoop()
