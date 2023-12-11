import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 타이틀 설정
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30
paddle_speed = 5  # 패들 속도를 느리게 설정

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = random.choice([-3, 3])  # 공 속도를 느리게 설정
ball_speed_y = -3  # 공 속도를 느리게 설정

# 블럭 설정
block_width = 70
block_height = 20
block_rows = 5
block_cols = 10
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * (block_width + 5)
        block_y = row * (block_height + 5) + 50
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# FPS 설정
clock = pygame.time.Clock()
fps = 60  # FPS를 낮춤으로써 게임을 느리게 실행

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽 충돌 체크
    if ball_x <= 0 or ball_x >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들 충돌 체크
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect((ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_speed_y = -ball_speed_y

    # 블럭 충돌 체크
    for block in blocks[:]:
        if pygame.Rect(block).colliderect((ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)

    # 게임 화면 그리기
    screen.fill(white)
    pygame.draw.rect(screen, black, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)
    for block in blocks:
        pygame.draw.rect(screen, black, block)

    pygame.display.update()

    # 게임 오버 체크
    if ball_y >= screen_height:
        running = False

    clock.tick(fps)  # FPS 설정을 반영

# 게임 종료
pygame.quit()
