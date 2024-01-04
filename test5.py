import turtle
import keyboard
import mouse
turtle.Screen()
drawer=turtle.Turtle()

while True:
    if keyboard.is_pressed('up'):
        drawer.forward(1.5)
    if keyboard.is_pressed('right'):
        drawer.right(5)
        if keyboard.is_pressed('up'):
             drawer.forward(5)
    if keyboard.is_pressed('left'):
        drawer.left(5)
        if keyboard.is_pressed('up'):
             drawer.forward(5)
             
    if mouse.is_pressed():
        break
    if keyboard.is_pressed('space'):
        drawer.clear()
  
