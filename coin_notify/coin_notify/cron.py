""" import sys
sys.path.append('../') """
from alert.send_mail import send_mail_if

def my_scheduled_job():
    send_mail_if()

if __name__ == "__main__":
    my_scheduled_job()
