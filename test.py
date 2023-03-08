import sys
import pygame

from Pysics import *

pygame.init()
size = width, height = 1200, 800

screen = pygame.display.set_mode(size)
pygame.display.set_caption("test for pysics")

clock = pygame.time.Clock()


def message(text, x, y, size, type):
    font = pygame.font.SysFont("Freesansbold", size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_surf, text_rect = text_surface, text_surface.get_rect()
    # x types
    if type[0] == "l":
        text_rect.x = x
    if type[0] == "c":
        text_rect.centerx = x
    if type[0] == "r":
        text_rect.right = x
    # y types
    if type[1] == "t":
        text_rect.y = y
    if type[1] == "c":
        text_rect.centery = y
    if type[1] == "b":
        text_rect.bottom = y
    screen.blit(text_surf, text_rect)


# 创建世界
w = World(screen)

# 导入模型
c = RenderModel("cube.md3")
cube = RigidBody3D(w, c, (1, 1, 1), 10, False)

# 键盘按键
keys = pygame.key.get_pressed()

# 移动相机
w.camera.move(-15, 0, 0)

while 1:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # 相应鼠标转动视角
        if event.type == pygame.MOUSEMOTION:
            direct = event.rel
            # 水平转动
            w.camera.rotate_horizontal(-direct[0] / 250)
            # 竖直转动
            w.camera.rotate_vertical(-direct[1] / 250)

    # 相应鼠标移动相机
    if keys[pygame.K_w]:
        w.camera.move(0.2, 0, 0)
    if keys[pygame.K_s]:
        w.camera.move(-0.2, 0, 0)
    if keys[pygame.K_a]:
        w.camera.move(0, -0.2, 0)
    if keys[pygame.K_d]:
        w.camera.move(0, 0.2, 0)
    if keys[pygame.K_SPACE]:
        w.camera.move(0, 0, 0.2)
    if keys[pygame.K_LSHIFT]:
        w.camera.move(0, 0, -0.2)

    pygame.mouse.set_pos(width / 2, height / 2)
    pygame.mouse.set_visible(False)

    screen.fill((255, 255, 255))
    w.update()
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (width / 2 - 10, height / 2),
        (width / 2 + 10, height / 2),
        2
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (width / 2, height / 2 - 10),
        (width / 2, height / 2 + 10),
        2
    )

    message(f"fps: {round(clock.get_fps())}", 10, 10, 30, ("l", "t"))
    message(f"sight: {w.camera.sight}", 10, 35, 30, ("l", "t"))
    message(f"pos: ({round(w.camera.pos[0], 3)}, "
            f"{round(w.camera.pos[1], 3)}, "
            f"{round(w.camera.pos[2], 3)})", 10, 60, 30, ("l", "t"))

    pygame.display.update()
    clock.tick(30)
