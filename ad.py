import machine
from machine import PWM, Pin
from time import sleep
import math
led = Pin(25, Pin.OUT)
led.toggle
l = 5
m = 5
x = 1
y = 1
shoulder = PWM(Pin(15))              
shoulder.freq(50)
shoulder.duty_u16(1500)
sleep(.01)
shoulder.duty_u16(5500)

def leg1 (x,y):
# a = math.pi / 6
#print (math.cos(a))
    q2 = math.acos((x^2 + y^2 - l^2 - m^2)/ (2 * l * m ))
    print (q2)
    q1 = math.atan(y / x) - math.atan((m * math.sin(q2) / (l + m * math.cos(q2))))
    print (q1)
    qq1 = int(1100 + q1 * 3750)
    qq2 = int(1100 + q2 * 3750)
    print (qq2)
    print (qq1)
    shoulder = PWM(Pin(15))
               
    shoulder.freq(50)
    shoulder.duty_u16(qq1)
    sleep(1)
    shoulder = PWM(Pin(14))
    shoulder.duty_u16(qq2)

led.toggle
def home ():
    shoulder = PWM(Pin(14))              
    shoulder.freq(50)
    shoulder.duty_u16(1500)
    sleep(.01)
    shoulder.duty_u16(5500)
    shoulder = PWM(Pin(15))              
    shoulder.freq(50)
    shoulder.duty_u16(1500)
    sleep(1)
    shoulder.duty_u16(5500)
    #leg1(1,1)
home ()

for i in range (1,9):
    #for j = in range (1,9):
        leg1 (i , i )
        sleep (0.01)
        home ()
        sleep (1)
        shoulder = PWM(Pin(15))              
        shoulder.freq(50)
        shoulder.duty_u16(2500)
        sleep(.01)
        shoulder.duty_u16(5100)
        shoulder = PWM(Pin(14))              
        shoulder.freq(50)
        shoulder.duty_u16(2000)
        sleep(1)
        shoulder.duty_u16(5600)
        sleep (0.1)
        



