def play_catch_apples2():
    from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
    from machine import Pin, PWM, ADC
    import random
    from time import sleep
    import math

    display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
    W, H = display.get_bounds()
    sky = display.create_pen(135, 206, 235)
    ground = display.create_pen(34, 139, 34)
    trunk = display.create_pen(101, 67, 33)
    fg = display.create_pen(240, 240, 240)
    apple_red = display.create_pen(220, 0, 0)
    apple_shadow = display.create_pen(160, 0, 0)
    stem_brown = display.create_pen(120, 70, 20)
    leaf_green = display.create_pen(0, 180, 60)
    highlight = display.create_pen(255, 200, 200)
    bg = display.create_pen(10, 10, 40)
    basket_light = display.create_pen(193, 154, 107)
    basket_dark = display.create_pen(140, 98, 57)
    basket_handle = display.create_pen(120, 80, 45)
    leaves_pen = display.create_pen(0, 180, 0)
    pwm = PWM(Pin(2))
    pwm.duty_u16(0)
    adc=ADC(26)

    def beep(freq, dur):
        pwm.freq(freq)
        pwm.duty_u16(32768)
        sleep(dur)
        pwm.duty_u16(0)
        sleep(0.05)

    def play_intro():
        melody = [
            (440, 0.3), (494, 0.3), (523, 0.3),
            (587, 0.3), (659, 0.3), (698, 0.3),
        ]
        for f, d in melody:
            beep(f, d)

    def draw_canopy_oval(cx, cy, rx, ry):
        display.set_pen(leaves_pen)
        for yy in range(cy - ry, cy + ry + 1):
            t = yy - cy
            v = ry * ry - t * t
            if v < 0: continue
            dx = int(rx * math.sqrt(v / (ry * ry)))
            x1 = max(0, cx - dx)
            x2 = min(W - 1, cx + dx)
            display.line(x1, yy, x2, yy)

    def draw_hollow_on_trunk(cx, cy, w, h):
        hollow_pen = display.create_pen(40, 20, 20)   
        border_pen = display.create_pen(80, 50, 30) 
        display.set_pen(hollow_pen)
        for yy in range(cy - h//2, cy + h//2):
            t = yy - cy
            v = (h//2) * (h//2) - t * t
            if v < 0: 
                continue
            dx = int((w//2) * math.sqrt(v / ((h//2) * (h//2))))
            display.line(cx - dx, yy, cx + dx, yy)
        display.set_pen(border_pen)
        display.circle(cx, cy, w//2)

    def draw_background_tree_with_apples():
        gy = (H * 4) // 5
        gh = H - gy
        display.set_pen(sky); display.rectangle(0, 0, W, H)
        display.set_pen(ground); display.rectangle(0, gy, W, gh)
        cx = W // 2
        cy = 60
        rx = W // 2 - 20
        ry = 50
        draw_canopy_oval(cx, cy, rx, ry)
        tx = cx - 14
        ty = cy + ry
        th = max(10, gy - ty)
        display.set_pen(trunk); display.rectangle(tx, ty, 28, th)
        draw_hollow_on_trunk(cx, ty + th//2, 18, 30)
        apple_positions = [
            (cx - 60, cy - 25), (cx - 40, cy - 28), (cx - 20, cy - 30),
            (cx + 20, cy - 30), (cx + 40, cy - 28), (cx + 60, cy - 25),
            (cx - 60, cy), (cx - 40, cy + 2), (cx - 20, cy),
            (cx + 20, cy), (cx + 40, cy + 2), (cx + 60, cy),
            (cx - 50, cy + 25), (cx - 30, cy + 28), (cx - 10, cy + 30),
            (cx + 10, cy + 30), (cx + 30, cy + 28), (cx + 50, cy + 25)
        ]

        for (ax, ay) in apple_positions:
            display.set_pen(stem_brown)
            display.line(ax, ay - 6, ax, ay - 2) 
            draw_apple(ax, ay, 6)
       
    def draw_background(): 
        gy = (H * 4) // 5 
        gh = H - gy 
        display.set_pen(sky); display.rectangle(0, 0, W, H) 
        display.set_pen(ground); display.rectangle(0, gy, W, gh) 
        display.set_pen(trunk); display.rectangle(80, 0, 80, 200)
        draw_hollow_on_trunk(W//2, 100, 50, 110)

    def draw_apple(cx, cy, r):
        display.set_pen(apple_red); display.circle(int(cx), int(cy), int(r))
        display.set_pen(apple_shadow); display.circle(int(cx - r*0.2), int(cy + r*0.15), int(r*0.8))
        display.set_pen(stem_brown); display.rectangle(int(cx - r*0.15), int(cy - r - r*0.2), int(r*0.3), int(r*0.5))
        lx1 = int(cx + r*0.15); ly1 = int(cy - r*0.2)
        lx2 = int(cx + r*0.9);  ly2 = int(cy - r*0.7)
        lx3 = int(cx + r*0.55); ly3 = int(cy - r*0.05)
        display.set_pen(leaf_green); display.triangle(lx1, ly1, lx2, ly2, lx3, ly3)
        display.set_pen(highlight); display.circle(int(cx + r*0.35), int(cy - r*0.25), int(r*0.25))

    def draw_basket(x, y, w, h):
        display.set_pen(basket_light); display.rectangle(int(x), int(y), int(w), int(h))
        display.set_pen(basket_dark); display.rectangle(int(x), int(y), int(w), int(h//5))
        step = 6
        for i in range(int(x) + step, int(x) + int(w), step):
            display.set_pen(basket_dark); display.line(i, int(y), i, int(y) + int(h))
        hx = int(x + w//2)
        display.set_pen(basket_handle); display.line(int(x), int(y), hx, int(y - h//2))
        display.set_pen(basket_handle); display.line(int(x + w), int(y), hx, int(y - h//2))

    r = 10
    a = 0
    display.set_pen(bg); display.clear(); draw_background_tree_with_apples(); display.update(); play_intro(); sleep(0.1)
    while adc.read_u16()>450:
        #print(adc.read_u16())
        display.set_pen(bg); display.clear(); display.set_pen(fg); display.text("Turn left pls", 15, 110, scale=3); display.update(); sleep(0.1)
    display.set_pen(bg); display.clear(); display.set_pen(fg); display.text("Get ready", 30, 100, scale=4); display.update(); sleep(2.5)
    display.set_pen(bg); display.clear(); display.set_pen(fg); display.text("Start", 40, 100, scale=6); display.update(); sleep(1)
    display.set_pen(bg); display.clear(); display.update(); sleep(0.01)
    q = 5
    basket_w = 50
    basket_h = 20
    basket_y = H - basket_h

    while True:
        x = random.randint(20, W - 20)
        y = 10
        draw_background()
        draw_apple(int(x), int(y), r)
        draw_basket(a, basket_y, basket_w, basket_h)
        display.update(); sleep(0.1)
        while y < H - 10:
            draw_background()
            y += q
            draw_apple(int(x), int(y), r)
            draw_basket(a, basket_y, basket_w, basket_h)
            display.update()
            sleep(0.001)
            a = adc.read_u16()/65535*190
        overlap_h = not ((x + r) < a or (x - r) > (a + basket_w))
        if overlap_h and (y + r) >= basket_y:
            pwm.freq(700); pwm.duty_u16(32768); sleep(0.1)
            draw_background(); draw_basket(a, basket_y, basket_w, basket_h); display.update()
            pwm.duty_u16(0)
            q += 1
        else:
            display.set_pen(bg); display.clear()
            pwm.freq(1000); pwm.duty_u16(32768)
            display.set_pen(fg); display.text("Game over :(", 5, 100, scale=4); display.update(); sleep(2)
            display.set_pen(bg); display.clear(); display.update(); sleep(0.01)
            score_text = "Score " + str(q - 5)
            scale = 6 if q < 15 else 5
            display.set_pen(fg); display.text(score_text, 20, 100, scale=scale); display.update(); sleep(0.1)
            pwm.duty_u16(0); sleep(0.01)
            break
        sleep(0.01)