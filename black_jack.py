def play_blackjack():
    from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
    from time import sleep
    from machine import Pin, PWM
    import random

    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["S","H","D","C"]

    pwm = PWM(Pin(2))
    pwm.duty_u16(0)

    def tone(f, d=200, duty=18000):
        pwm.freq(f)
        pwm.duty_u16(duty)
        sleep(d/1000)
        pwm.duty_u16(0)

    display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
    W, H = display.get_bounds()
    bg = display.create_pen(0, 0, 0)
    white = display.create_pen(255, 255, 255)
    green = display.create_pen(0, 200, 0)
    red = display.create_pen(255, 80, 80)
    yellow = display.create_pen(255, 220, 0)
    gray = display.create_pen(90, 90, 90)

    B = Pin(13, Pin.IN, Pin.PULL_UP)
    Y = Pin(15, Pin.IN, Pin.PULL_UP)

    def btn(p):
        return p.value() == 0

    def wait_btn(*buttons):
        while True:
            for b in buttons:
                if btn(b):
                    sleep(0.15)
                    return b

    def create_deck():
        deck = [(r, s) for s in suits for r in ranks]
        for i in range(len(deck) - 1, 0, -1):
            j = random.randint(0, i)
            deck[i], deck[j] = deck[j], deck[i]
        return deck

    def hand_value(hand):
        total = 0
        aces = 0
        for r, _ in hand:
            if r in ["J","Q","K"]:
                total += 10
            elif r == "A":
                total += 11
                aces += 1
            else:
                total += int(r)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def deal(deck, n=1):
        out = deck[:n]
        del deck[:n]
        return out

    def draw_text(t, x, y, scale=2, pen=white):
        display.set_pen(pen)
        display.text(t, x, y, W-10, scale)

    def draw_suit(s, x, y, sz, pen_light, pen_dark):
        if s in ("H", "D"):
            display.set_pen(red)
        else:
            display.set_pen(white)
        if s == "H":
            display.circle(int(x - sz*0.5), int(y), int(sz*0.5))
            display.circle(int(x + sz*0.5), int(y), int(sz*0.5))
            display.triangle(int(x - sz), int(y), int(x + sz), int(y), int(x), int(y + int(sz*1.2)))
        elif s == "D":
            display.triangle(int(x), int(y - sz), int(x - sz), int(y), int(x + sz), int(y))
            display.triangle(int(x), int(y + sz), int(x - sz), int(y), int(x + sz), int(y))
        elif s == "C":
            display.circle(int(x), int(y - sz*0.6), int(sz*0.5))
            display.circle(int(x - sz*0.7), int(y + sz*0.2), int(sz*0.5))
            display.circle(int(x + sz*0.7), int(y + sz*0.2), int(sz*0.5))
            display.set_pen(white)
            display.rectangle(int(x - sz*0.25), int(y + sz*0.3), int(sz*0.5), int(sz*0.9))
        elif s == "S":
            display.circle(int(x - sz*0.5), int(y), int(sz*0.5))
            display.circle(int(x + sz*0.5), int(y), int(sz*0.5))
            display.triangle(int(x - sz), int(y), int(x + sz), int(y), int(x), int(y - int(sz*1.2)))
            display.set_pen(white)
            display.rectangle(int(x - sz*0.25), int(y + sz*0.2), int(sz*0.5), int(sz*0.9))

    def draw_card(r, s, x, y, scale_rank=2):
        draw_text(r, x, y - 10, scale_rank, white)
        draw_suit(s, x + 24, y - 6, 10, white, red)

    def draw_hand(cards, x, y, hide_second=False):
        if hide_second and len(cards) >= 2:
            r1, s1 = cards[0]
            draw_card(r1, s1, x, y)
            display.set_pen(gray)
            display.rectangle(x + 56, y - 16, 42, 34)
        else:
            cx = x
            for r, s in cards:
                draw_card(r, s, cx, y)
                cx += 56

    def render(player, dealer, hide_dealer=True, msg=""):
        display.set_pen(bg); display.clear()
        draw_text("Dealer:", 10, 5, 2, green)
        draw_hand(dealer, 10, 40, hide_second=hide_dealer)
        dv = "?" if hide_dealer else str(hand_value(dealer))
        draw_text("Total: " + dv, 10, 60, 2)
        draw_text("You:", 10, 120, 2, green)
        draw_hand(player, 10, 150, hide_second=False)
        draw_text("Total: " + str(hand_value(player)), 10, 160, 2)
        if msg:
            draw_text(msg, 10, 210, 2, red)
        display.update()

    def player_turn(deck, player, dealer):
        render(player, dealer, True, "B=Hit  Y=Stand")
        while True:
            b = wait_btn(B, Y)
            if b is B:
                tone(900, 80)
                player += deal(deck, 1)
                render(player, dealer, True, "B=Hit  Y=Stand")
                if hand_value(player) > 21:
                    tone(250, 220)
                    return player, "bust"
            else:
                tone(650, 80)
                return player, "stand"

    def dealer_turn(deck, dealer):
        while hand_value(dealer) < 17:
            dealer += deal(deck, 1)
            render([], dealer, False)
            sleep(0.25)
        return dealer

    def result_msg(player, dealer):
        pv = hand_value(player)
        dv = hand_value(dealer)
        if pv > 21:
            return "You lose :("
        if pv==21 and dv!=21:
            return "BLACKJACK! <3"
        if dv > 21:
            return "You win :)"
        if pv > dv:
            return "You win :)"
        if pv < dv:
            return "You lose :("
        return "Push :')"

    def play_hand(deck):
        if len(deck) < 15:
            deck[:] = create_deck()
        player = deal(deck, 2)
        dealer = deal(deck, 2)
        render(player, dealer, True, "B=Hit  Y=Stand")
        if hand_value(player) == 21 and hand_value(dealer) != 21:
            tone(1200, 160)
            render(player, dealer, False, "BLACKJACK! <3")
            return
        if hand_value(player) == 21 and hand_value(dealer) == 21:
            render(player, dealer, False, "Push :')")
            return
        player, state = player_turn(deck, player, dealer)
        if state == "bust":
            render(player, dealer, False, "Bust :(")
            return
        dealer = dealer_turn(deck, dealer)
        msg = result_msg(player, dealer)
        if "win" in msg.lower():
            tone(1000, 120); tone(1300, 120)
        elif "lose" in msg.lower():
            tone(300, 220)
        else:
            tone(1200, 160)
        render(player, dealer, False, msg)


    display.set_pen(bg); display.clear()
    display.set_pen(red); display.text("BLACK", 25, 110, scale=4); display.set_pen(white); display.text("JACK", 135, 110, scale=4); display.update(); sleep(0.01)

    draw_suit("H", 70, 50, 30, white, red); tone(523); display.update(); sleep(0.2)
    draw_suit("C", 180, 50, 30, white, red); tone(587); display.update(); sleep(0.2)
    draw_suit("D", 70, 190, 30, white, red); tone(659); display.update(); sleep(0.2)
    draw_suit("S", 180, 190, 30, white, red); tone(698); display.update(); sleep(0.2)

    display.update()
    sleep(1)
    display.set_pen(bg); display.clear()

    deck = create_deck()
    play_hand(deck)