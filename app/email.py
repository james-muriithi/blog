from flask_mail import Message
from flask import render_template, current_app
from decouple import config
from . import mail
from time import sleep  
from threading import Thread  

def send_async_email(app, msg):
    with app.app_context():
        # block only for testing parallel thread
        for i in range(10, -1, -1):
            sleep(2)
            print('time:', i)
        print('====> sending async')
        mail.send(msg)


def mail_message(subject,template,to,**kwargs):
    app = current_app._get_current_object()
    sender_email = config("MAIL_USERNAME", default="")

    msg = Message(subject, sender=("Epic Blogs"), recipients=[to])
    msg.html = render_template(template + ".html",**kwargs)

    thr = Thread(target=send_async_email, args=[app, msg])

    thr.start()
    return thr