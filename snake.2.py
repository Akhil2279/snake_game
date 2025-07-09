import turtle
import time
import random

# Game Setup
delay = 0.1
game_running = True

window = turtle.Screen()
window.title('SNAKE XANIA – Neon Edition')
window.bgcolor('#1a1a2e')  # Midnight background
window.setup(width=600, height=600)
window.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('#e94560')  # Neon red
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('#ffd369')  # Yellow gold
food.penup()
food.goto(0, 100)

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0", align='center', font=('Arial', 24, 'bold'))

# Game Over Message
def show_game_over():
    pen.goto(0, 0)
    pen.write("GAME OVER\nPress 'R' to Restart", align='center', font=('Arial', 20, 'bold'))

# Movement Functions
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'

# Restart the Game
def restart_game():
    global score, delay, game_running
    head.goto(0, 0)
    head.direction = 'stop'
    for segment in body:
        segment.goto(1000, 1000)
    body.clear()
    score = 0
    delay = 0.1
    pen.clear()
    pen.goto(0, 260)
    pen.write(f"SCORE: {score}", align='center', font=('Arial', 24, 'bold'))
    game_running = True

# Handle R key
def handle_restart():
    if not game_running:
        pen.clear()
        restart_game()

# Keyboard Bindings
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')
window.onkeypress(handle_restart, 'r')

# Body Segments and Score
body = []
score = 0

# Main Game Loop
while True:
    window.update()

    if not game_running:
        continue

    # Wall Collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_running = False
        show_game_over()

    # Food Collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('#00adb5' if len(body) % 2 == 0 else '#393e46')
        new_segment.penup()
        body.append(new_segment)
        score += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"SCORE: {score}", align='center', font=('Arial', 24, 'bold'))

    # Move body segments
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
    if body:
        body[0].goto(head.xcor(), head.ycor())

    move()
    time.sleep(delay)

    # Self-Collision
    for segment in body:
        if segment.distance(head) < 20:
            game_running = False
            show_game_over()
