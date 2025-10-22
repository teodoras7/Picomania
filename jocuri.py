from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from time import sleep
from machine import Pin, PWM
from utime import ticks_ms

pwm = PWM(Pin(2))
pwm.duty_u16(0)
def tone(freq_hz, d=32768):
    pwm.freq(freq_hz)
    pwm.duty_u16(d)

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
W, H = display.get_bounds()
bg = display.create_pen(0, 0, 0)
green = display.create_pen(0, 200, 0)
blue = display.create_pen(0, 120, 255)
red = display.create_pen(255, 0, 0)
yellow = display.create_pen(255, 220, 0)
white = display.create_pen(255, 255, 255)

A = Pin(12, Pin.IN, Pin.PULL_UP)
B = Pin(13, Pin.IN, Pin.PULL_UP)
X = Pin(14, Pin.IN, Pin.PULL_UP)
Y = Pin(15, Pin.IN, Pin.PULL_UP)

def btn(p):
    return p.value() == 0

def wait_any():
    while True:
        if btn(A): tone(800); sleep(0.05); pwm.duty_u16(0); return "A"
        if btn(B): tone(800); sleep(0.05); pwm.duty_u16(0); return "B"
        if btn(X): tone(800); sleep(0.05); pwm.duty_u16(0); return "X"
        if btn(Y): tone(800); sleep(0.05); pwm.duty_u16(0); return "Y"

def wait_choice(keys):
    while True:
        k = wait_any()
        if k in keys:
            return k

def msg(text, pen=white, y=100, scale=2, clear=True):
    if clear:
        display.set_pen(bg); display.clear()
    display.set_pen(pen)
    display.text(text, 16, y, scale=scale)
    display.update()

def menu_screen():
    display.set_pen(bg); display.clear()
    display.set_pen(green); display.text("A: Simon Says", 20, 30, scale=2)
    display.set_pen(blue); display.text("B: Be Fast", 20, 80, scale=2)
    display.set_pen(red); display.text("X: Catch Apples", 20, 130, scale=2)
    display.set_pen(yellow); display.text("Y: Blackjack", 20, 180, scale=2)
    display.update()

def submenu_simon():
    display.set_pen(bg); display.clear()
    display.set_pen(green); display.text("A: 5 levels", 20, 70, scale=2)
    display.set_pen(red); display.text("B: infinite loop", 20, 160, scale=2)
    display.update(); sleep(0.1)
    k = wait_choice({"A","B"})
    if k == "A":
        import simon_says
        simon_says.play_simon_says()
    else:
        import simon_says_loop
        simon_says_loop.play_simon_says_loop()

def submenu_be_fast():
    display.set_pen(bg); display.clear()
    display.set_pen(yellow); display.text("A: solo", 20, 70, scale=2)
    display.set_pen(blue); display.text("B: 1v1", 20, 160, scale=2)
    display.update(); sleep(0.1)
    k = wait_choice({"A","B"})
    if k == "A":
        import be_fast
        be_fast.play_be_fast()
    else:
        import be_fast_1v1
        be_fast_1v1.play_be_fast_1v1()

def submenu_catch():
    display.set_pen(bg); display.clear()
    display.set_pen(red); display.text("A: buttos", 20, 70, scale=2)
    display.set_pen(blue); display.text("B: potentiometer", 20, 160, scale=2)
    display.update(); sleep(0.1)
    k = wait_choice({"A","B"})
    if k == "A":
        import catch_apples
        catch_apples.play_catch_apples()
    else:
        import catch_apples2
        catch_apples2.play_catch_apples2()

def run_selected(key):
    if key == "A":
        submenu_simon()
    elif key == "B":
        submenu_be_fast()
    elif key == "X":
        submenu_catch()
    elif key == "Y":
        import black_jack
        black_jack.play_blackjack()

display.set_pen(blue); display.text("PI", 20, 100, scale=4); display.update(); tone(261); sleep(0.4)
display.set_pen(blue); display.text("CO", 60, 100, scale=4); display.update(); tone(523); sleep(0.4)
display.set_pen(blue); display.text("MA", 105, 100, scale=4); display.update(); tone(294); sleep(0.4)
display.set_pen(blue); display.text("NI", 150, 100, scale=4); display.update(); tone(587); sleep(0.4)
display.set_pen(blue); display.text("A", 190, 100, scale=4); display.update(); tone(329); sleep(0.4)

def wait():
    last_time=ticks_ms()
    while ticks_ms() - last_time < 10000:
            if X.value() == 0:
                return True
            sleep(0.01)
    return False 

while True:
    pwm.duty_u16(0); sleep(1); 
    menu_screen()
    key = wait_any()
    ok2=1
    ok1=1
    while True:
        run_selected(key)
        last_time=ticks_ms()
        ok1=1
        while ticks_ms() - last_time < 10000 and ok1 and ok2:
            if X.value() == 0:
                ok1=0
            if A.value() == 0:
                ok2=0
            sleep(0.01)
        if ok1:
            break
    if ok2==1:
        break