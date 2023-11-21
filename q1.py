import turtle

screen = turtle.Screen()
drone = turtle.Turtle()

drone.left(90)

left_pressed = False
right_pressed = False

def rotate_left():
    global left_pressed
    left_pressed = True
    while left_pressed:
        drone.left(3)  

def rotate_right():
    global right_pressed
    right_pressed = True
    while right_pressed:
        drone.right(3) 

def stop_rotate_left():
    global left_pressed
    left_pressed = False

def stop_rotate_right():
    global right_pressed
    right_pressed = False

def move_forward():
    drone.forward(20)  

def move_backward():
    drone.backward(20) 

def reset_position():
    drone.goto(0, 0)  
    drone.left(90)  
    drone.clear()  

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(reset_position, "r")  
screen.onkeypress(rotate_left, "a")  
screen.onkeypress(rotate_right, "d") 
screen.onkeyrelease(stop_rotate_left, "a")  
screen.onkeyrelease(stop_rotate_right, "d")  

screen.onclick(turtle.bye)

screen.mainloop()
