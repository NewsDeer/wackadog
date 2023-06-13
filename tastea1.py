import machine
from machine import PWM, Pin
from time import sleep

left = PWM(Pin(14))              
left.freq(50)
left.duty_u16(5500)

shoulder = PWM(Pin(15))              
shoulder.freq(50)
shoulder.duty_u16(5500)