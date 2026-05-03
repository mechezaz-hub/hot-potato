timer = 0

def on_button_pressed_a():
    global timer
    timer = randint(10, 100)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
    while timer > 0:
        timer += -1
        basic.pause(1000)
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.A, on_button_pressed_a)
