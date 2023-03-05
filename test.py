import sys
import pygame

from Pysics import *

pygame.init()
size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("test for pysics")

# 创建世界
w = World(screen)

# 导入模型
cube = RenderModel("cube.md3")

# 键盘按键
keys = pygame.key.get_pressed()

# 移动相机
w.camera.move(-5, 0, 0)

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
    pygame.display.update()
