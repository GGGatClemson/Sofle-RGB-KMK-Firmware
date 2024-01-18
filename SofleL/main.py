import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

#Git test
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

layers_ext = Layers()

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.TX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP29, board.GP28, None, False),)

keyboard.modules = [layers_ext, split, encoder_handler]
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.STATIC,1:["Sofle v2"]},
        corner_four={0:OledReactionType.LAYER,1:["Base","Code","League","FPS"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)
# Layer Keys
HOLDCHANGE = KC.MO(1)
TOGGLELOL = KC.TG(2)
TOGGLEVAL = KC.TG(3)
TOGGLERNG = KC.TG(5)

# Cool Keys
KILL = KC.LALT(KC.LCTL(KC.DEL))
HELMET = KC.LALT(KC.N5)
# keymap 
keyboard.keymap = [

    # Default Keymap
    [
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSLS,

        KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,

        KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,

        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,

        KC.LGUI, KC.LALT, KC.LCTL, HOLDCHANGE, KC.LALT, KC.LALT(KC.LCTL(KC.DEL)), KC.B, KC.ENT, KC.SPC, KC.BSLS,
        KC.RALT, KC.RGUI,

        # Hopefully Encoder Rotate Input

    ],

    # Main Modified Keymap
    [KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F0, KC.TILDE,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LBRC, KC.UP, KC.RBRC, KC.TRNS, KC.TRNS,
     KC.LALT(KC.TAB), KC.LPRN, KC.RPRN, KC.MINS, KC.EQL, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, TOGGLELOL, TOGGLEVAL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

     # Hopefully Encoder Rotate Inputs
     ],

    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        HELMET, KC.L, KC.LCTL, KC.SPC, KC.LALT, TOGGLELOL, KC.TRNS, KC.Y, KC.Y, KC.TRNS, KC.TRNS, KC.TRNS,
    ],

    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
     KC.N4, KC.N3, KC.V, KC.N1, KC.N2, TOGGLEVAL, TOGGLEVAL, KC.LALT, KC.Y, KC.TRNS, KC.TRNS, KC.TRNS,
     ]
]
# keymap
keyboard.extensions.append(oled_ext)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),(KC.VOLD, KC.VOLU)),  # base layer
    ((KC.VOLD, KC.VOLU)),  # Raise
    ((KC.VOLD, KC.VOLU)),  # Lower
]

keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
