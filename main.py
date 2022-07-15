import json
from config import URL, API_KEY, RULES
import requests
from sendemail import send_email


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
        keyfile = open(f'saved_file/{file_name}.json', "w")
        keyfile.write(json.dumps(file_input))
        keyfile.close()


if __name__ == "__main__":

    json_result = json.loads(api_result())
    print(json_result)
    if RULES["save"]:
        commit_rules_save(json_result["timestamp"], json_result["rates"])
    if RULES["email"]["enable"]:
        send_email(json_result['rates'])
