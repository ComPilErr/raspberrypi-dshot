import dshot
import time
"""
Speed-up and slow-down motor rapidly on pin 5 with telemetry request on maximum speed point
"""

MAX_SPEED = 2000
MIN_SPEED = 50
NULL_SPEED = 48
PIN_OUT = 5
Dt = 12
increment = 30
NO_TELEM = 0
ON_TELEM = 1

t = time.time()*1000
t1=t
speed = NULL_SPEED


for _ in range(10000):
    dshot.send(NULL_SPEED, PIN_OUT, NO_TELEM)
    time.sleep(0.00012)

while(1):
    t = time.time()*1000
    if (abs(t-t1)>Dt):
        dshot.send(speed, PIN_OUT, NO_TELEM)
        t1=t
        speed += increment
        if(increment>0):
            print("Increase: ", speed)
        if(increment<0):
            print("Decrease: ", speed)
        if(speed>MAX_SPEED):
            increment = (-1)*increment
            speed += increment
            dshot.send(speed, PIN_OUT, ON_TELEM)
            time.sleep(0.00012)
            speed += increment
        if(speed<MIN_SPEED):
            increment = (-1)*increment
            speed += increment
            dshot.send(NULL_SPEED, PIN_OUT, NO_TELEM)
            time.sleep(0.00012)
            speed += increment
            for _ in range(9999):
                dshot.send(NULL_SPEED, PIN_OUT, NO_TELEM)
                time.sleep(0.00012)
            break

