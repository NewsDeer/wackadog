import machine
from machine import PWM, Pin
from time import sleep

shoulder = PWM(Pin(15))              
shoulder.freq(50)
shoulder.duty_u16(7000)
sleep(1)
shoulder.duty_u16(6000)
shoulder = PWM(Pin(14))              
shoulder.freq(50)
    shoulder.duty_u16(6000)
    sleep(0.1)
    shoulder = PWM(Pin(14))
    shoulder.freq(50)
    shoulder.duty_u16(2400)
    
    print("restarting")
    legtest()
legtest()