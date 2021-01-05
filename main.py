import turtle
import random
from tkinter import messagebox
#Fuctions
def go_right():
	x = paddle.xcor()
	x = x + 8
	paddle.setx(x)

def go_left():
	x = paddle.xcor()
	x = x - 8
	paddle.setx(x)




#Main Window
wn = turtle.Screen()
wn.title("Breakgame")
wn.setup(800,600)# (x , y) 
wn.bgpic("bg.gif")



#register shapes
wn.register_shape("bg.gif")
wn.register_shape("ball.gif")	
wn.register_shape("paddle.gif")



#Brick lists
bricks = []

#Color lists
colors = ["#0C5D3F" , "#FF7C28" , "#FF6CC3" , "#40BED5"]

#Ball number
balls = 2



#Paddle
class Paddle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shapesize(stretch_wid=1 , stretch_len=5)
		self.color("red")
		self.shape("paddle.gif")
		self.speed(0)
		self.goto(0, -260)

#Ball
class Ball(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.color("red")
		self.shape("ball.gif")
		self.speed(0)
		self.goto(0, 0)
		self.dx = 4
		self.dy = 4
		
#Bricks
# Add bricks 
for _ in range (6):
	brick = turtle.Turtle()
	brick.speed(0)  
	brick.shape("square")
	brick.shapesize(stretch_wid=1 , stretch_len=4)
	brick.color(random.choice(colors))
	brick.penup()
	brick.speed(0)
	x = random.randint(-360 , 360)
	y = random.randint(0 ,280 )
	brick.goto(x , y)
	bricks.append(brick)




#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0 , 260)
font = ("Courier" , "24" , "normal")
pen.write(f"Balls:{balls} " , align = "center"  , font = font)
















#Keybinding
wn.listen()
wn.onkeypress(go_right , "Right")
wn.onkeypress(go_left , "Left")



#Calling classes
paddle = Paddle()
ball = Ball()


#Main game loop
while True:
	wn.update()
	#global x 
	#global y
	
	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#check if ball is on the corners
	if ball.ycor() >= 290:
		ball.sety(290)
		ball.dy *= -1
	

	if ball.xcor() >= 390:
		ball.setx(390)
		ball.dx *= -1
	
	if ball.xcor() <= -390:
		ball.setx(-390)
		ball.dx *= -1
	
	
	# check if ball going out
	if ball.ycor() < -290:
		ball.goto(0,0)
		ball.dy *= -1
		balls -= 1
		pen.clear()
		pen.write(f"{balls} " , align = "center"  , font = font)
	#Paddle and ball collisions
	if ball.ycor() < -260 and (ball.xcor() < paddle.xcor() + 40 and ball.xcor() > paddle.xcor() - 40):
		ball.dy *= -1
	
	# Bricks settings
	for brick in bricks:
		#check if collision with bricks
		if ball.distance(brick) <= 50:
			brick.goto(2000,200)
			ball.dy *= -1

		
	#Loosong state
	if balls <= 0:
		messagebox.showinfo(title = "Info" , message = "You loose!")
		wn.close()
		
	




wn.mainloop()
