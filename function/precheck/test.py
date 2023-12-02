import requests

def handler(event, context):
    print(event)

    res = requests.get('https://checkip.amazonaws.com')

    return res.text