import json
from config import URL, API_KEY, RULES
import requests
from khayyam import JalaliDatetime
from sms import check_notify_rules, send_sms
from sendemail import send_email


def iran_time():
    time = JalaliDatetime.now()
    return f'{time.year}/{time.month}/{time.day}'


def api_result():
    """
    getting json from site and reading it
    """
    payload = {}
    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", URL, headers=headers, data=payload)

    status_code = response.status_code

    if status_code == 200:
        return response.text
    else:
        print("error in finding file")


def commit_rules_save(file_name, file_input):
    """
    saving file in saves_file
    """
    keyfile = open(f'saved_file/{file_name}.json', "w")
    keyfile.write(iran_time() + json.dumps(file_input))
    keyfile.close()


if __name__ == "__main__":
    json_result = json.loads(api_result())
    print(api_result())
    if RULES["save"]:
        commit_rules_save(json_result["timestamp"], json_result["rates"])
    if RULES["email"]["enable"]:
        send_email(json_result['rates'])
    if RULES['notification']['enable']:
        notification_msg = check_notify_rules(json_result["rates"])
        if notification_msg:
            send_sms(notification_msg)
