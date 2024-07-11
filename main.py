import turtle
import random
import time
import threading

turtle_screen = turtle.Screen()
turtle_screen.title("Catch The Turtle")
turtle_screen.bgcolor("Light blue")

turtle_instance = turtle.Turtle()
turtle_instance.color("Deep pink3")

turtle_instance.shape("turtle")
turtle_instance.shapesize(2)
turtle_instance.penup()
turtle_instance.speed(6)

countdown = 15
pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()

score = 0
pen2 = turtle.Turtle()
pen2.color("black")
pen2.hideturtle()

def update_score(x, y):
    global score
    score += 1
    x = 0
    y = 0

pen2.clear()
pen2.penup()
pen2.setposition(0, 350)
pen2.write(f"Score: {score}", align="center", font= (None,15))

def turtle_timer():
    for timer in range(countdown, -1, -1):
        pen.clear()
        pen.penup()
        pen.speed("fastest")
        pen.setposition(0, 320)
        pen.write(f"Timer: {timer}", align= "center", font= (None,15))
        time.sleep(1)


turtles = []
def moving_turtle():
    for i in range(30):
        a = random.randint(-200, 200)
        b = random.randint(-200, 200)
        turtle_instance.hideturtle()
        turtle_instance.setposition(a, b)
        turtle_instance.showturtle()
        turtle_screen.delay(95)
        turtle_instance.setposition(a, b)

turtle_screen.listen()
turtle_instance.onclick(update_score)
turtles.append(turtle_instance)

countdown_thread = threading.Thread(target=turtle_timer)
turtle_thread = threading.Thread(target=moving_turtle)

countdown_thread.start()
turtle_thread.start()



turtle_screen.mainloop()
