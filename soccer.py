import random

WIDTH = 540
HEIGHT = 360

background = Actor('soccerbackground')

ball = Actor('ball')
ball.pos = WIDTH / 2, 0
ball.vy = 0
gravity = 360
score = 0
timer = 30

goal = Rect((225, 350), (60, 20))

def draw():
    background.draw()
    ball.draw()
    screen.draw.filled_rect(goal, 'white')

    score_string = str(score)
    screen.draw.text(score_string, (0, 0), color = 'white')

    time_string = str(round(timer))
    screen.draw.text(time_string, (50, 0), color = 'white')


def update(delta):
    global score, timer
    timer = timer - delta

    if timer <= 0:
        exit()

    ball.vy = ball.vy + gravity
    ball.y = ball.y + ball.vy

    if keyboard.left:
        goal.x = goal.x - 5
    elif keyboard.right:
        goal.x = goal.x + 5


    if ball.y > HEIGHT:
        ball.x = random.randint(80, 540)
        ball.y = 0

    if ball.colliderect(goal):
        ball.x = random.randint(80, 540)
        ball.y = 0
        score = score + 1
    reset()

def reset():
    ball.vy = 0
    gravity = 5

reset()
