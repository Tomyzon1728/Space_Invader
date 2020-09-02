# Code by A•R•T

# importing necessary modules
import turtle
import os
import random

# screen properties
screen= turtle.Screen()
screen.title("Space Invader Game")
screen.bgcolor("black")

# defining border
border=turtle.Turtle()
border.speed(0)
border.color("yellow")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Creating the Player
player=turtle.Turtle()
player.color("green")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)

player_speed=15

# Creating players bullets
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheadint(90)
bullet.shapesize(0.3,0.3)
bullet.hideturtle()

bullet_speed=20

# Defining the state of the bullet
# READY : is ready to fire 
# FIRE : bullet is firing 
bullet_state= "ready"

# Creating the Enemy
enemy= turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemy_speed=2

#L-R Player movement
def left():
    x_lmove= player.xcor()
    x_lmove -= player_speed
    # To restrict left border movement 
    if x_lmove < -280:
        x_lmove= -280
    player.setx(x_lmove)

def right():
    x_rmove= player.xcor()
    x_rmove += player_speed
    # To restrict right border movement
    if x_rmove > 280:
        x_rmove = 280
    player.setx(x_rmove)
    
def bullet():
    # Defining bullet_state as global should in case there's need for change 
    global bullet_state
    if bullet_state== "fire":
        bullet_state= "ready "
    
    
        # Moving the bullet just above the player
        x =player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
    
    
# Creating Keyboard binding
turtle.listen()
turtle.onkeypress(left,"l")
turtle.onkeypress(right,"r")
turtle.onkeypress(bullet, "space")
                 
# Game loop
while True:
    # Moving the enemy 
    x = enemy.xcor()  
    x+=enemy_speed
    enemy.setx(x)
    
    # Moving the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y-= -40
        enemy_speed*= -1
        enemy.sety(y)
        
    if enemy.xcor() < -280:
        y= enemy.ycor()
        y-= - 40
        enemy_speed = -1
        enemy.sety(y)
        
    # Moving the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y+= bullet_speed
        bullet.sety(y)
        
    # checking if bullet is at the top
    if bullet.ycor() > 275:
        bullet.hideturtle()

screen.mainloop()