import json
from property import URL, API_KEY, RULES
import requests
import smtplib


def api_result():
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
    if RULES["SAVE"]:
        keyfile = open(f'saved_file/{file_name}.json', "w")
        keyfile.write(json.dumps(file_input))
        keyfile.close()


def send_email(rates):
    sender = "babakft082@gmail.com"
    receiver = "babakft082@gmail.com.com"

    message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

{rates}."""
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("261f765550ac77", "669f7100c11602")
        server.sendmail(sender, receiver, message)


if __name__ == "__main__":
    result = api_result()
    json_result = json.loads(result)
    print(result)
    commit_rules_save(json_result["timestamp"], json_result["rates"])
    send_email(json_result['rates'])
