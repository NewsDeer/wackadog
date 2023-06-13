
from machine import PWM, Pin
from time import sleep
led = Pin(25, Pin.OUT)
led.toggle()
shoulder = PWM(Pin(15))
               
shoulder.freq(50)
shoulder.duty_u16(1500)
sleep(1)
shoulder.duty_u16(5500)
shoulder = PWM(Pin(14))
               
shoulder.freq(50)
shoulder.duty_u16(1500)
sleep(1)
shoulder.duty_u16(5500)
