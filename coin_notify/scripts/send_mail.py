from alert import models
import requests
import inspect
from django.core.mail import send_mail

def get_rate_BTC():
    """
    Make a request to coinapi to get Bitcoin current USD value
    """
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : 'BF00CAD7-3171-4359-9FF3-AE20F922F5C5'}
    response = requests.get(url, headers=headers)
    return response.json()

def send(alert, response):
    """
    Format and send the email
    """
    if alert.bigger_than == 1:
        msg = ("""Hello %s.\n\nThis is an email to alert you that bitcoin """
            """rate get beyond %s USD today %s""" %(
            alert.owner, alert.value, response['time']))
    else:
        msg = ("""Hello %s.\n\nThis is an email to alert you that bitcoin """
            """rate fell below %s USD today %s""" %(
            alert.owner, alert.value, response['time']))
    send_mail(
        'CoinNotify',
        msg,
        'coinnotify42@gmail.com',
        [alert.owner.email],
        fail_silently=False,
    )

def send_mail_if():
    """
    Get bitcoin current value and compare it to all alert.
    Call send() and delete the alert if the alert conditions are positive 
    """
    response = get_rate_BTC()
    queryset = models.Alert.objects.all()
    for alrt in queryset:
        if (alrt.bigger_than == 1 and alrt.value < response['rate']) \
        or (alrt.bigger_than == 0 and alrt.value > response['rate']):
            send(alrt, response)
            alrt.delete()
        
