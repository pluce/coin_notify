from alert import models
import requests

def get_rate_BTC():
    """
    Make a request to coinapi to get Bitcoin current USD value
    """
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : 'BF00CAD7-3171-4359-9FF3-AE20F922F5C5'}
    response = requests.get(url, headers=headers)
    return response.json()['rate']

def send_mail(alert, rate):
    print("sending mail to %s for alert value = %f" % (alert.owner.email, alert.value) )

def send_mail_if():
    response = get_rate_BTC()
    print("BTC rate = %d" % (response))
    queryset = models.Alert.objects.all()
    for alrt in queryset:
        if (alrt.bigger_than == 1 and alrt.value < response) \
        or (alrt.bigger_than == 0 and alrt.value > response):
            send_mail(alrt, response)
        

def run():
    send_mail_if()