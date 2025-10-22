def play_be_fast():
    from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
    from time import sleep
    from machine import Pin, PWM
    import random
    import sys
    from utime import ticks_ms

    pwm = PWM(Pin(2))
    pwm.duty_u16(0)
    def tone(freq_hz, duty=32768):
        pwm.freq(freq_hz)
        pwm.duty_u16(duty)

    display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
    W, H = display.get_bounds()
    bg = display.create_pen(0, 0, 0)
    green = display.create_pen(0, 200, 0)
    blue = display.create_pen(0, 120, 255)
    red = display.create_pen(255, 0, 0)
    yellow = display.create_pen(255, 220, 0)
    white = display.create_pen(255, 255, 255)

    A= Pin(12, Pin.IN, Pin.PULL_UP)
    B= Pin(13, Pin.IN, Pin.PULL_UP)
    X= Pin(14, Pin.IN, Pin.PULL_UP)
    Y= Pin(15, Pin.IN, Pin.PULL_UP)

    display.set_pen(bg); display.clear(); sleep(0.01)

    display.set_pen(green); display.rectangle(0, 0, 120, 120); tone(261); display.set_pen(white); display.text("C4", 25, 40, scale=7); display.update(); sleep(0.5)
    display.set_pen(red); display.rectangle(120, 0, 120, 120); tone(329); display.set_pen(white); display.text("E4", 145, 40, scale=7); display.update(); sleep(0.5)
    display.set_pen(blue); display.rectangle(0, 120, 120, 120); tone(294); display.set_pen(white); display.text("D4", 25, 160, scale=7); display.update(); sleep(0.5)
    display.set_pen(yellow); display.rectangle(120, 120, 120, 120); tone(349); display.set_pen(white); display.text("F4", 145, 160, scale=7); display.update(); sleep(0.5)

    pwm.duty_u16(0); sleep(1.5)
    display.set_pen(bg); display.clear()
    display.set_pen(white); display.text("Get ready", 30, 100, scale=4); display.update(); sleep(2.5)
    display.set_pen(bg); display.clear()
    display.set_pen(white); display.text("Start", 40, 100, scale=6); display.update(); sleep(1)
    display.set_pen(bg); display.clear(); display.update(); sleep(0.01)

    x=[random.randint(1, 4) for _ in range(1000)]

    def loose(j):
        display.set_pen(white); display.rectangle(int(0), int(0), int(240), int(240)); tone(988)
        display.update()
        sleep(2)
        pwm.duty_u16(0); display.set_pen(bg); display.rectangle(int(0), int(0), int(240), int(240)); display.update()
        display.set_pen(white); display.text("Game over :(", 5, 100, scale=4); display.update(); sleep(2)
        display.set_pen(bg); display.rectangle(int(0), int(0), int(240), int(240)); display.update()
        sleep(0.01)
        if j<10:
            display.set_pen(white); display.text("Score " + str(j), 20, 100, scale=6); display.update(); sleep(0.1)
        else:
            display.set_pen(white); display.text("Score " + str(j), 20, 100, scale=5); display.update(); sleep(0.1)

    i=0; j=5000

    ok=1
    while ok:  
        if x[i] == 1:
            display.set_pen(green); display.rectangle(0, 0, 120, 120)
        elif x[i] == 2:
            display.set_pen(blue); display.rectangle(0, 120, 120, 120)
        elif x[i] == 3:
            display.set_pen(red); display.rectangle(120, 0, 120, 120)
        elif x[i] == 4:
            display.set_pen(yellow); display.rectangle(120, 120, 120, 120)
        display.update()
        last_time = ticks_ms()
        while True:
            if A.value():
                pwm.duty_u16(0)
            elif x[i] == 1:
                tone(261)
                sleep(0.3)
                i += 1
                pwm.duty_u16(0); display.set_pen(bg); display.clear; display.update()
                sleep(0.01)
                break
            else :
                loose(i); ok=0; break 
            if B.value():
                pwm.duty_u16(0)
            elif x[i] == 2:
                tone (294); sleep(0.3)
                i += 1
                pwm.duty_u16(0); display.set_pen(bg); display.rectangle(int(0), int(0), int(240), int(240)); display.update()
                sleep(0.01)
                display.set_pen(bg); display.clear()
                break
            else :
                loose(i); ok=0; break   
            if X.value():
                pwm.duty_u16(0)
            elif x[i] == 3:
                tone (329)
                sleep(0.3)
                i += 1
                pwm.duty_u16(0); display.set_pen(bg); display.rectangle(120, 0, 120, 120); display.update()
                sleep(0.01)
                display.set_pen(bg); display.clear()
                break
            else :
                loose(i); ok=0; break  
            if Y.value():
                pwm.duty_u16(0)
            elif x[i] == 4:
                tone (349)
                sleep(0.3)
                i += 1
                pwm.duty_u16(0); display.set_pen(bg); display.rectangle(int(0), int(0), int(240), int(240)); display.update()
                sleep(0.01)
                display.set_pen(bg); display.clear()
                break
            else :
                loose(i); ok=0; break
            if ticks_ms() - last_time > j:
                loose(i); ok=0; break
        if ok:
            pwm.duty_u16(0); display.set_pen(bg); display.rectangle(int(0), int(0), int(240), int(240)); display.update()
            sleep(round(random.uniform(0, j/1000), 1))
            display.set_pen(bg); display.clear()
            j -= 100