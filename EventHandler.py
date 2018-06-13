import libtcodpy as libtcod

##Returns the key that is currently pressed down as a string
def return_key():

    key_pressed = "null"

    key = libtcod.console_wait_for_keypress(True)

    #Check All The Arrow Keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        key_pressed = "KEY_UP"
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        key_pressed = "KEY_DOWN"
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        key_pressed = "KEY_RIGHT"
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        key_pressed = "KEY_LEFT"

    #Check for Character Keys
    key_char = chr(key.c)
    if key_char == 'k':
        key_pressed = "k"

    elif key_char =='i':
        key_pressed = "i"

    elif key_char == '1':
        key_pressed = '1'

    return key_pressed
