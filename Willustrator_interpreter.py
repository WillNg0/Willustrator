import turtle
from textx import metamodel_from_file

screen = turtle.Screen()
screen.title("Willustrator")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)


def draw_line(l):
    compass = l.direction.compass
    if compass == 'N':
        pen.setheading(90)
    elif compass == 'NE':
        pen.setheading(45)
    elif compass == 'NW':
        pen.setheading(135)
    elif compass == 'S':
        pen.setheading(270)
    elif compass == 'SE':
        pen.setheading(315)
    elif compass == 'SW':
        pen.setheading(225)
    elif compass == 'E':
        pen.setheading(0)
    elif compass == 'W':
        pen.setheading(180)
    elif hasattr(l.direction, "angle"):
        if l.direction.angle.turn == "right":
            pen.right(l.direction.angle.degrees)
        elif l.direction.angle.turn == "left":
            pen.left(l.direction.angle.degrees)

    pen.forward(l.length)
    
def draw_shape(shape):
    pen.down()
    pen.begin_fill()
    if shape.line_color is not None:
        pen.pencolor(shape.line_color.color)
    else:
        pen.pencolor('black')
    if shape.fill_color.color is not None:
        pen.fillcolor(shape.fill_color.color)
    else:
        pen.fillcolor('white')
    
    for l in shape.lines:
        draw_line(l)

    pen.end_fill()

def write_fizzbuzz(l):
    for i in range(l.begin, l.end):
        if i % 3 == 0 and i % 5 == 0:
            text = "FizzBuzz"
        elif i % 3 == 0:
            text = "Fizz"
        elif i % 5 == 0:
            text = "Buzz"
        else:
            text = str(i)

        pen.write(text, font=(l.font, l.size, "normal"))
        pen.sety(pen.ycor() - 20)

willustrator_mm = metamodel_from_file("willustrator.tx")
canvas = willustrator_mm.model_from_file("dog.wlstr")

for c in canvas.draw_instructions: 
    pen.up()
    if hasattr(c, "position") and c.position is not None:
        pen.goto(c.position.x, c.position.y)
    else:
        pen.goto(0, 0)

    if c.__class__.__name__ == "FizzBuzz":
        pen.color("black")
        write_fizzbuzz(c)
    else:
        draw_shape(c.shape)
turtle.done()