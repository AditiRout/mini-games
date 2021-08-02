import turtle
import random
import time
delay=0.1
win=turtle.Screen()
win.title("snake game")
win.bgcolor("black")
win.setup(800,600)
win.tracer(0)


score=0
food=turtle.Turtle()
food.penup()
food.goto(0,0)
food.pendown
food.shape("circle")
food.color("white")
food.speed(0)


head=turtle.Turtle()
head.penup()
head.goto(0,100)
head.pendown()
head.color("red")
head.shape("square")
head.penup()
head.speed(0)
head.direction="Stop"

pen=turtle.Turtle()

pen.penup()
pen.hideturtle()
pen.goto(0,320)
pen.color("white")
pen.write("score:0",align="center",font=("Arial",24,"bold"))
pen.speed(0)


def goup():
    if head.direction!="down":
         head.direction="up"
def godown():
    if head.direction!="up":
        head.direction="down"
def goleft():
    if head.direction!="right":
        head.direction="left"
def goright():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

win.listen()
win.onkeypress(goup,"w")
win.onkeypress(godown,"s")
win.onkeypress(goleft,"a")
win.onkeypress(goright,"d")

parts=[]

while True:
    win.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>390 or head.ycor()<-390:
        time.sleep(1)
        head.goto(0,100)
        head.direction = "stop"
        for part in parts:
            part.goto(1000, 1000)
        part.clear()
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Arial", 20, "normal"))

    if head.distance(food)<20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

       
        part = turtle.Turtle()
        part.speed(0)
        part.shape("square")
        part.color("orange")
        part.penup()
        parts.append(part)

        delay-=0.01

        score+=10
        pen.clear()
        pen.write("Score: {} ".format(score), align="center", font=("Arial", 20, "normal"))

    for i in range(len(parts)-1,0,-1):
        x=parts[i-1].xcor()
        y=parts[i-1].ycor()
        parts[i].goto(x,y)

    if len(parts)>0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x,y)

    move()

    for part in parts:
        if part.distance(head)<20:
            time.sleep(1)
            head.goto(0,100)
            head.direction = "stop"
            for part in parts:
                part.goto(1000, 1000)
            part.clear()
            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Arial", 20, "normal"))


    time.sleep(delay)
            
    

        
        
    
    

    



    
    
    
    








