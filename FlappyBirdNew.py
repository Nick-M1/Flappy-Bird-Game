import pygame, random

pygame.init()
screen_width = 500
screen_height = 550
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FLAPPY BIRD")
font = pygame.font.SysFont("comicsans", 30, True)
hitSound = pygame.mixer.Sound("Resources/RightHook.wav.wav")

bg = pygame.image.load('Resources/flappybird_bg')
bg = pygame.transform.scale(bg, (700, 550))
bg_x1, bg_x2, p_x = 0, 700, 700

x, y, width, height, vel = 70, 250, 50, 50, 15
isJump = False
jumpCount = 10
list_of_obstacle = []
score = 0

pic1, pic2, pic3, pic4 = pygame.image.load('Resources/sprite10.png'), pygame.image.load('Resources/sprite20.png'), pygame.image.load(
    'Resources/sprite30.png'), pygame.image.load('Resources/sprite40.png')
bird_pic = [pygame.transform.scale(pic1, (50, 50)), pygame.transform.scale(pic2, (50, 50)),
            pygame.transform.scale(pic3, (50, 50)), pygame.transform.scale(pic4, (50, 50))]
bird_num = 0


def draw_pillars():
    global x, y, run, width, score
    pillar_gap = 150
    for j in list_of_obstacle:
        pygame.draw.rect(win, (99, 196, 106), (j[0], 0, 50, (j[1] - pillar_gap)))         # Top
        pygame.draw.rect(win, (99, 196, 106), (j[0] - 10, j[1] - pillar_gap - 20, 70, 20))
        pygame.draw.rect(win, (99, 196, 106), (j[0], j[1], 50, (490 - j[1])))             # Bottom
        pygame.draw.rect(win, (99, 196, 106), (j[0] - 10, j[1], 70, 20))
        j[0] -= 5

        if j[0] - 40 <= x <= (j[0] + 60) and j[1] - width <= y <= 550:                  # Bottom
            print("You lose")
            hitSound.play()
            run = False
        elif j[0] - 40 <= x <= (j[0] + 60) and 0 <= y <= j[1] - pillar_gap - 10:             # Top
            print("You lose")
            hitSound.play()
            run = False
        elif j[0] - 40 <= x <= (j[0] + 60):
            score += 1


for i in range(50):
    list_of_obstacle.append([p_x, random.choice(range(150, 450))])
    p_x += 350

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not isJump:
        bird_num = 0
        if keys[pygame.K_SPACE]:
            isJump = True
            bird_num = 1
        else:
            y += vel
    else:
        if jumpCount >= -2:
            bird_num = 2
            neg = 1
            if jumpCount < 0:
                bird_num = 3
                neg = -1
            y -= ((jumpCount ** 2) * 0.25 * neg - 2)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if bg_x1 <= -800:
        bg_x1 = 570
    else:
        bg_x1 -= 5

    if bg_x2 <= -800:
        bg_x2 = 570
    else:
        bg_x2 -= 5

    win.fill((0, 0, 0))
    win.blit(bg, (bg_x1, 0))
    win.blit(bg, (bg_x2, 0))
    win.blit(bird_pic[bird_num], (x, y))
    draw_pillars()
    text = font.render("Score: " + str(int(score/21)), 1, (0, 0, 0))
    win.blit(text, (360, 10))
    if y > 520:
        run = False

    pygame.display.update()

pygame.quit()

print("Your final score is", str(int(score/21)))
