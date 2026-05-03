let timer = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    timer = randint(10, 100)
    basic.showIcon(IconNames.Chessboard)
    basic.showArrow(ArrowNames.SouthEast)
    while (timer > 0) {
        timer += -1
        basic.pause(1000)
    }
    basic.showIcon(IconNames.Skull)
})
