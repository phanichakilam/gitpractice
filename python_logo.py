import turtle
import time

def setup_screen(title):
    turtle.clear()
    turtle.speed(8)
    turtle.title(title)
    turtle.bgcolor("white")
    turtle.pensize(5)

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_python_logo():
    setup_screen("Python Logo")

    # Draw top (blue)
    turtle.color("#306998")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.circle(50, 90)
    turtle.forward(50)
    turtle.circle(50, 90)
    turtle.forward(100)
    turtle.circle(50, 90)
    turtle.forward(50)
    turtle.circle(50, 90)
    turtle.end_fill()
    draw_circle("white", 30, 40, 10)

    # Draw bottom (yellow)
    turtle.color("#FFD43B")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(50, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.circle(50, 90)
    turtle.forward(50)
    turtle.circle(50, 90)
    turtle.forward(100)
    turtle.circle(50, 90)
    turtle.forward(50)
    turtle.circle(50, 90)
    turtle.end_fill()
    draw_circle("white", 130, -40, 10)

    turtle.hideturtle()
    time.sleep(2)

def draw_devops_infinity():
    setup_screen("DevOps Infinity Symbol")

    turtle.color("purple")

    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.left(45)
    for _ in range(2):
        turtle.circle(50, 180)
        turtle.circle(25, 180)

    turtle.hideturtle()
    time.sleep(2)

def draw_cloud(name):
    setup_screen(f"{name} Cloud Symbol")

    turtle.color("skyblue")

    turtle.penup()
    turtle.goto(-70, -30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.goto(70, -30)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(-100, -60)
    turtle.pendown()
    turtle.forward(200)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-30, -100)
    turtle.pendown()
    turtle.write(name, font=("Arial", 18, "bold"))

    turtle.hideturtle()
    time.sleep(2)

def main():
    draw_python_logo()
    draw_devops_infinity()
    draw_cloud("AWS")
    draw_cloud("Azure")
    draw_cloud("GCP")

    turtle.done()

if __name__ == "__main__":
    main()
