import machine
from machine import PWM, Pin
from time import sleep
led = Pin(25, Pin.OUT)
led.toggle()
shoulder = PWM(Pin(14))
shoulder.freq(50)

elbow = PWM(Pin(15))
elbow.freq(50)

def play_bow():
    shouder.duty_u16(3000)
    elbow.duty_u16(3000)
    
def stand():