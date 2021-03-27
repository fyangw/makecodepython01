i = 9
j = 1

def on_button_pressed_a():
    global i
    i = i + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global j
    j = j + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global i, j
    k = i + j
    basic.show_string(" " + i + "+" + j + "=" + k)
basic.forever(on_forever)
