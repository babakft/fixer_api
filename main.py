import json
from property import URL, API_KEY, RULES
import requests


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


if __name__ == "__main__":
    result = api_result()
    json_result = json.loads(result)
    print(result)
    commit_rules_save(json_result["timestamp"], json_result["rates"])

