input.onButtonPressed(Button.A, function () {
    i = i + 1
})
input.onButtonPressed(Button.B, function () {
    j = j + 1
})
let k = 0
let j = 0
let i = 0
i = 9
j = 1
basic.forever(function () {
    k = i + j
    basic.showString(" " + i + "+" + j + "=" + k)
})
