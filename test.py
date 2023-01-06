import sys

from Render.world import *
from Render.camera import *

pygame.init()
clock = pygame.time.Clock()
size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("test for pysics")
w = World(screen)
c = w.camera

# Tunnel
# for i in range(0, 127):
#     Point3D((i * 2, 1, 1), color = (i * 2, 0, 255 - 1 * 2))
#     Point3D((i * 2, 1, -1), color = (i * 2, 0, 255 - 1 * 2))
#     Point3D((i * 2, -1, 1), color = (i * 2, 0, 255 - 1 * 2))
#     Point3D((i * 2, -1, -1), color = (i * 2, 0, 255 - 1 * 2))

# Test
# Point3D((3, 0, 1))

# Cube
Point3D((5, 1, 1), size=5)
Point3D((5, 1, -1), size=5)
Point3D((5, -1, 1), size=5)
Point3D((5, -1, -1), size=5)
Point3D((7, 1, 1), size=5)
Point3D((7, 1, -1), size=5)
Point3D((7, -1, 1), size=5)
Point3D((7, -1, -1), size=5)

keys = []

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys.append(event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            keys.remove(event.key)

    screen.fill((255, 255, 255))
    c.show()
    pygame.display.update()
    clock.tick(40)
