from pynput import mouse
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

def on_move(x, y):
    if config.getboolean('Events', 'move'):
        print('Pointer moved to {0}'.format(
            (x, y)))
    
def on_click(x, y, button, pressed):
    if config.getboolean('Events', 'click'):
        if pressed:
            print(str(button)+ " pressed at ("+str(x)+", "+str(y)+")")
        else:
            print(str(button)+ " released at ("+str(x)+", "+str(y)+")")
    
def on_scroll(x, y, dx, dy):
    if config.getboolean('Events', 'scroll'):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
