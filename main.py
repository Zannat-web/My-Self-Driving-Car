import pygame
pygame.init()
window = pygame.display.set_mode((504, 360))

track = pygame.image.load('track.png.png')
car = pygame.image.load('car.png.jpg')

car = pygame.transform.scale(car, (30, 60))
car = pygame.transform.rotate(car, -90)
car_x = 340
car_y = 36
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'right'
drive = True
clock = pygame.time.Clock()

while drive:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    cam_x = car_x + cam_x_offset + 50
    cam_y = car_y + cam_y_offset + 15
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]

    # GOING RIGHT(initial state)
    if direction == "right" and right_px == 0:
        car_x = car_x + 2

    # DOWN TURN
    elif direction == "right" and right_px != 0 and down_px == 0:
        direction = "down"
        car_x = car_x + 25
        cam_x_offset = -35
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

    # GOING DOWN
    elif direction == "down" and right_px != 16 and down_px == 0:
        car_y = car_y + 2

    # LEFT TURN
    elif direction == "down" and down_px != 0 and left_px == 0:
        direction = "left"
        cam_y_offset = 0
        car_y = car_y + 25
        car = pygame.transform.rotate(car, -90)

    # GOING LEFT
    elif direction == "left" and down_px != 16 and left_px == 0 or left_px == 25:
        car_x = car_x - 2

    # UP TURN
    elif direction == "left" and left_px != 0 and up_px == 0:
        direction = "up"
        cam_x_offset = -35
        cam_y_offset = -5
        car = pygame.transform.rotate(car, -90)

    # GOING UP
    elif direction == "up" and left_px != 0 and up_px == 0:
        car_y = car_y - 2

    # RIGHT TURN
    elif direction == "up" and right_px == 0:
        direction = "right_last"
        cam_y_offset = 0
        cam_x_offset = 0
        car_y = car_y -7
        car = pygame.transform.rotate(car, -90)

    # GOING RIGHT
    elif direction == "right_last" and right_px == 0:
        car_x = car_x + 2

    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 4, 4)
    pygame.display.update()