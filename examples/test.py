from machine import UART
from picaso_lcd import display
from picaso_lcd import colors


import math
import time


def demo_sine(disp, color):
    max_x, max_y = disp.get_display_size()

    f = lambda x: math.sin(x / 10.0) * max_y / 2 + max_y / 2
    for i in range(1, max_x):
        disp.gfx_line(i - 1, int(f(i - 1)), i, int(f(i)), color)


def demo_text(disp, color, rgb_color):
    disp.text.set_size(2)
    disp.text.set_fg_color(color)
    disp.text.put_string("Whole Lotta Rosie\n")
    disp.text.set_size(1)
    disp.text.put_string(f"{rgb_color} - {color:016b}\n")
    disp.text.put_string(
        "Wanna tell you a story\n'Bout a woman I know\nWhen it comes to lovin'"
        "\nOh, she steals the show\nShe ain't exactly pretty\nShe ain't exactly small\n"
        "42-39-56\nYou could say she's got it all!\n\n"
        "Never had a woman, never had a woman like you\n"
        "Doin' all the things, doin' all the things you do\n"
        "Ain't no fairy story\n"
        "Ain't no skin-and-bones\n"
        "But you give all you got, weighin' in at nineteen stone"
    )


def demo_text_pos(disp, x, y, color):
    disp.text.set_size(1)
    disp.text.set_fg_color(color)
    disp.text.move_origin(x, y)
    disp.text.put_string(f"({x},{y})")


# If read timeout is it may cause errors
uart = UART(1, 9600, rx=19, tx=21)
uart.init(9600, bits=8, parity=None, stop=1, timeout=1000)


disp = display.Display(uart)
time.sleep(3)
disp.cls()
disp.set_orientation(1)
disp.set_contrast(15)
disp.set_background_color(colors.WHITE)

# 115200
try:
    disp.set_baudrate(13)
except:
    # With changed baudrate we will get errors in response
    pass
uart.init(115200, bits=8, parity=None, stop=1, timeout=1000)

colors_list = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
]
cur_color = 0

while True:
    demo_text(
        disp, colors.to_16bit_color(colors_list[cur_color]), colors_list[cur_color]
    )
    time.sleep(3)
    disp.cls()

    demo_text_pos(disp, 10, 50, colors.to_16bit_color(colors_list[cur_color]))
    demo_text_pos(disp, 100, 50, colors.to_16bit_color(colors_list[cur_color]))
    demo_text_pos(disp, 10, 100, colors.to_16bit_color(colors_list[cur_color]))
    demo_text_pos(disp, 100, 100, colors.to_16bit_color(colors_list[cur_color]))
    time.sleep(2)
    disp.cls()

    demo_sine(disp, colors.to_16bit_color(colors_list[cur_color]))
    time.sleep(2)

    disp.set_contrast(0)  # off
    time.sleep(2)
    disp.set_contrast(1)  # on
    time.sleep(2)

    disp.cls()
    disp.gfx_circle(100, 100, 10, colors.ALICEBLUE, filled=True)
    disp.gfx_circle(200, 100, 10, colors.ALICEBLUE, filled=True)
    disp.gfx_polyline(
        [(120, 100), (130, 110), (140, 115), (150, 115), (160, 110), (170, 100)],
        colors.BLUE,
    )
    disp.gfx_rect(200, 120, 300, 200, colors.DARKBLUE, filled=True)
    time.sleep(2)
    disp.cls()

    cur_color += 1
    cur_color = cur_color % len(colors_list)
