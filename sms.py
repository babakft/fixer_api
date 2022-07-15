from config import RULES
from kavenegar import *


def check_notify_rules(rates):
    """
    check for statement in max and min
    """
    preferred = RULES['notification']['preferred']
    msg = ''
    for exc in preferred:
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min: {rates[exc]} \n'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max: {rates[exc]} \n'

    return msg


def send_sms(text):
    # sending with kavenegar sms service
    try:
        api = KavenegarAPI('35724E6C3853776741684A4F723043596970797778643354334B736D4B566A5976633449646B62365930633D')
        params = {'sender': '100047778', 'receptor': {RULES['notification']['receiver']}, 'message': {text}}
        response = api.sms_send(params)
        print(response)
    except Exception as error:
        print(error)