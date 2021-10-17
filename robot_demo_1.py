from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
from time import sleep

forward_r = 16
backward_r = 26
forward_l = 5
backward_l = 6
en_r = 12
en_l = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(forward_r,GPIO.OUT)
GPIO.setup(forward_l,GPIO.OUT)
GPIO.setup(backward_r,GPIO.OUT)
GPIO.setup(backward_l,GPIO.OUT)
GPIO.setup(en_r, GPIO.OUT)
GPIO.setup(en_l, GPIO.OUT)

GPIO.output(forward_r,GPIO.LOW)
GPIO.output(backward_r,GPIO.LOW)
GPIO.output(forward_l,GPIO.LOW)
GPIO.output(backward_l,GPIO.LOW)

p = GPIO.PWM(en_r,65)
q = GPIO.PWM(en_l,55)

GPIO.setwarnings(False)

def aage():
    GPIO.output(forward_r,GPIO.HIGH)
    GPIO.output(backward_r,GPIO.LOW)
    GPIO.output(forward_l,GPIO.HIGH)
    GPIO.output(backward_l,GPIO.LOW)
    
def peeche():
    GPIO.output(forward_r,GPIO.LOW)
    GPIO.output(backward_r,GPIO.HIGH)
    GPIO.output(forward_l,GPIO.LOW)
    GPIO.output(backward_l,GPIO.HIGH)
    
def right():
    GPIO.output(forward_r,GPIO.LOW)
    GPIO.output(backward_r,GPIO.HIGH)
    GPIO.output(forward_l,GPIO.HIGH)
    GPIO.output(backward_l,GPIO.LOW)
    
def left():
    GPIO.output(forward_r,GPIO.HIGH)
    GPIO.output(backward_r,GPIO.LOW)
    GPIO.output(forward_l,GPIO.LOW)
    GPIO.output(backward_l,GPIO.HIGH)

def stop():
    GPIO.output(forward_r,GPIO.LOW)
    GPIO.output(backward_r,GPIO.LOW)
    GPIO.output(forward_l,GPIO.LOW)
    GPIO.output(backward_l,GPIO.LOW)

def dpad(pos):
    if pos.top:
        aage()
        print("up")
    elif pos.bottom:
        peeche()
        print("down")
    elif pos.right:
        left()
        print("right")
    elif pos.left:
        right()
        print("left")
    elif pos.middle:
        stop()
        print("stop")

bd = BlueDot()
bd.when_pressed = dpad

pause()