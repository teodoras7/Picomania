from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from time import sleep

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
W, H = display.get_bounds()
display.create_pen(0, 0, 0); display.clear(); display.update(); sleep(0.1)