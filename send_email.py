import smtplib
import ssl


HOST_NAME = "smtp.gmail.com"
PORT = 465
USER_NAME = "cap8.chirag@gmail.com"
PWD = "xsat ryrd acdf xmae"


def sendemail(receiver, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(HOST_NAME,PORT, context=context) as server:
        server.login(USER_NAME, PWD)
        server.sendmail(USER_NAME, receiver, message)





