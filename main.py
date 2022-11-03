import machine
import utime


led_blue = machine.Pin(20, machine.Pin.OUT) #blue
led_green = machine.Pin(19, machine.Pin.OUT) #green
led_red = machine.Pin(18, machine.Pin.OUT) #red
button = machine.Pin(23, machine.Pin.IN)


while True:
    #Grøn
    tid=0
    led_blue.value(1)
    led_green.value(0)
    led_red.value(1)
    #led_green.toggle() #green
    while tid<3600: #grøn
        utime.sleep(1)
        tid=tid+1
        if button.value() ==0:
            blue=1
            break
    #rød
    led_green.value(1)
    led_red.value(0)
    tid=0
    while button.value() ==0:
        pass
    while tid<3600: #rød
       utime.sleep(1)
       tid=tid+1
       if button.value() ==0:
           blue=1
           break
    while button.value() ==0:
        pass
    #rød blink
    tid=0
    while tid<15000: 
       utime.sleep(0.2)
       led_red.toggle()
       tid=tid+1
       if button.value() ==0:
           blue=1
           break
    while button.value() ==0:
        pass
    #rød/grøn blink
    tid=0
    while tid<7500: 
       utime.sleep(0.2)
       led_red.toggle()
       utime.sleep(0.2)
       led_green.toggle()
       tid=tid+1
       if button.value() ==0:
           blue=1
           break
    while button.value() ==0:
        pass
    #Blå
    blue;
    led_green.value(1)
    led_red.value(1)
    led_blue.value(0)
    tid=0
    while button.value() ==0:
        pass
    while tid<3600: #blå
       utime.sleep(1)
       tid=tid+1
       if button.value() ==0: break
    while button.value() ==0:
        pass
    utime.sleep(0.2)  
    #blå blink
    while button.value() ==1: #blink blå
      led_blue.toggle()
      utime.sleep(0.2)
    while button.value() ==0:
      vent=0 #gør ingen ting
    utime.sleep(0.2)