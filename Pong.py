import turtle
import os
import math
import random

cursor_size = 20
player_height = 60
player_width = 20

court_width = 1000
court_height = 600


#screen
wn = turtle.Screen()
wn.title("PingPangPong")
wn.bgcolor("black")
wn.setup(width = 1.0, height = 1.0)

#bordure
bordure = turtle.Turtle()
bordure.penup()
bordure.color("white")
bordure.pensize(3)
bordure.ht() 
def bordure1():
        bordure.setposition(-court_width/2, court_height/2)
        bordure.speed(5)
        bordure.pendown()
        bordure.fd(court_width)
        bordure.pu()
        bordure.sety(-court_height/2)
        bordure.pd()
        bordure.backward(court_width)
def filet():
    bordure.pensize(1)
    bordure.setposition(0, -court_height/2)
    bordure.setheading(90)
    for i in range (court_height //50):
        bordure.fd(50/2+1)
        bordure.penup()
        bordure.fd(50/2+1)
        bordure.pendown()
bordure1()
filet()
#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ballspeed = 8
ball.penup()
ball.speed(0)

def start():
        ball.setposition(0,0)
        ball.setheading(random.choice([0,180])+ random.randint(-60, 60))
start()

#Player 1
player1 = turtle.Turtle()
player1.shape("square")
player1.turtlesize(player_height/cursor_size, player_width/cursor_size)
player1.color("white")
player1.penup()
player1.setx(cursor_size-court_width/2)
player1.speed(0)
playerspeed = 50

#Player 1 Movement
def up():
        y = player1.ycor()
        y += playerspeed
        if y < court_height/2:
                player1.sety(y)

def down():
        y = player1.ycor()
        y -= playerspeed
        if y > -court_height/2:
                player1.sety(y) 

#Player 2

player2 = turtle.Turtle()
player2.shape("square")
player2.shapesize(player_height/cursor_size, player_width / cursor_size)
player2.color("white")
player2.penup()
player2.setx(court_width/2+cursor_size)
player2.speed(0)
playerspeed = 50

#Player 2 movement
def up1():
        y = player2.ycor()
        y += playerspeed
        if y < court_height/2:
                player2.sety(y)

def down1():
        y = player2.ycor()
        y -= playerspeed
        if y > -court_height/2:
                player2.sety(y)             

#Speed hack
def hack():
        global ballspeed
        if ballspeed == 8:
                ballspeed = 20
        elif ballspeed == 20:
                ballspeed = 8

def restart():
        ball.setheading(random.choice([0,180])+ random.randint(-60, 60))
        ball.setposition(0, 0)


def distance(t1,t2):
        distance1 = t1.distance(t2)
        
        if distance1 < player_height/2:
                t2.setheading(180 -t2.heading())
                t2.fd(ballspeed)
                
#We assign z/s to move the player 1
wn.listen()
wn.onkey(up, "z")
wn.onkey(down,"s")
#We assign up and down arrow to move the player 2
wn.onkey(up1, "Up")
wn.onkey(down1,"Down")
#SpeedHack
wn.onkey(hack, "m")
#Restart
wn.onkey(start,"p")
#Player 2 score's
Score1 = 0
s1 = turtle.Turtle()
s1.speed(0)
s1.ht()
s1.color("white")
s1.pu()
s1.setposition(-250, 250)
s1.write(Score1, font=("Arial", 44, "normal"))
#Player 2 score's
Score2 = 0
s2 = turtle.Turtle()
s2.speed(0)
s2.ht()
s2.color("white")
s2.pu()
s2.setposition(250, 250)
s2.write(Score1, font=("Arial", 44, "normal"))

#Mainloop
def game():
        ball.fd(ballspeed)
        y = ball.ycor()
        x = ball.xcor()
        global Score1, Score2
#We define the border colision 
        if y > court_height/2 -cursor_size or y < cursor_size -court_height/2:
                 ball.setheading(-ball.heading())
#We define Loose              
        if x > court_width/2+20:
                Score1 += 1
                s1.clear()
                s1.write(Score1, font=("Arial", 44, "normal"))
                start()
        elif x < -court_width/2-20:
                Score2 += 1
                s2.clear()
                s2.write(Score2, font=("Arial", 44, "normal"))
                start()
        
#Colision beetween players and ball                
        distance(player1,ball)
        distance(player2,ball)
        wn.ontimer(game, 1)

game()

wn.mainloop()





