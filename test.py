import sys

from Pysics import *

pygame.init()
clock = pygame.time.Clock()
size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("test for pysics")
w = World(screen)

# Tunnel
# for i in range(0, 127):
#     Point3D((i * 2, 1, 1), color = (i * 2, 0, 255 - 1 * 2), size = 2)
#     Point3D((i * 2, 1, -1), color = (i * 2, 0, 255 - 1 * 2), size = 2)
#     Point3D((i * 2, -1, 1), color = (i * 2, 0, 255 - 1 * 2), size = 2)
#     Point3D((i * 2, -1, -1), color = (i * 2, 0, 255 - 1 * 2), size = 2)

# pyramid
# pyramid = Model3D().get_file("pyramid.md3")

cube = Model3D().get_file("cube.md3")
cube.move((2, 0, 0))
cube.move((2, 2, 0))
cube.move((2, 0, 2))
cube.move((2, 2, 2))
cube.move((0, 2, 0))
cube.move((0, 0, 2))
cube.move((0, 2, 2))

keys = pygame.key.get_pressed()
while 1:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            direct = event.rel
            w.camera.rotate(-direct[1] / 150, -direct[1] / 150)

    if keys[pygame.K_w]:
        w.camera.move(0.1, 0, 0)
    if keys[pygame.K_s]:
        w.camera.move(-0.1, 0, 0)
    if keys[pygame.K_a]:
        w.camera.move(0, -0.1, 0)
    if keys[pygame.K_d]:
        w.camera.move(0, 0.1, 0)
    if keys[pygame.K_SPACE]:
        w.camera.move(0, 0, 0.1)
    if keys[pygame.K_LSHIFT]:
        w.camera.move(0, 0, -0.1)

    screen.fill((255, 255, 255))
    w.camera.show()
    pygame.display.update()
    clock.tick(40)
