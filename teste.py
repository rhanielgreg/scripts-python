import time
import threading
from pynput.mouse import Button as bt, Controller as ct
from pynput.keyboard import Listener, KeyCode as kc
delay = 0.3
button = bt.left
start_stop_key = kc(char = 'a')
stop_key = kc(char = 'b')

class ClickMouse(threading.Thread):


    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    
    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False
    
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
mouse = ct()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):

    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    

    elif key == stop_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()