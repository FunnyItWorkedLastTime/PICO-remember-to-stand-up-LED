import machine
import utime


led_blue = machine.Pin(20, machine.Pin.OUT) #blue
led_green = machine.Pin(19, machine.Pin.OUT) #green
led_red = machine.Pin(18, machine.Pin.OUT) #red
button = machine.Pin(23, machine.Pin.IN)
global blue

def vent():
  tid=0
  while tid<3600: #rød
   utime.sleep(1)
   tid=tid+1
   if button.value() ==0: blaa()
  return

def blaa():
    led_green.value(1)
    led_red.value(1)
    led_blue.value(0)
    tid=0
    while tid<3600:
     utime.sleep(1)
     tid=tid+1
    #blå blink
    while True:
      led_blue.toggle()
      utime.sleep(0.2)
    return	

while True:
    #Grøn
    led_blue.value(1)
    led_green.value(0)
    led_red.value(1)
    vent()
    #rød
    led_green.value(1)
    led_red.value(0)
    vent()
    #rød blink
    tid=0
    while tid<18000: 
       utime.sleep(0.2)
       led_red.toggle()
       tid=tid+1
       if button.value() ==0: blaa()
    #rød/grøn blink
    tid=0
    while tid<10000: 
       led_red.value(0)
       utime.sleep(0.3)
       led_red.value(1)
       led_green.value(0)
       utime.sleep(0.3)
       led_green.value(1)
       led_blue.value(0)
       utime.sleep(0.3)
       led_blue.value(1)
       tid=tid+1
       if button.value() ==0: break
    blaa()
     


    
