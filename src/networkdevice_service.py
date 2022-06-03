import json

import requests


def call_api(ticket_id):
    api_url = "http://localhost:58000/api/v1/network-device"
    headers = {"X-Auth-Token": ticket_id}
    return requests.get(api_url, headers=headers, verify=False)


def get_networkdevices(ticket_id):
    resp = call_api(ticket_id)
    response_json = resp.json()
    networkdevices = response_json["response"]
    formatted_networkdevices = []
    for networkDevice in networkdevices:
        if "hostname" in networkDevice:
            formatted_networkdevices.append(format_dict_to_list(networkDevice))
        else:
            continue
    return formatted_networkdevices


def add_networkdevice(ticket_id):
    api_url = "http://localhost:58000/api/v1/network-device"

    headers = {"X-Auth-Token": ticket_id, 'Content-Type': 'application/json'}
    body = {
        "ipAddress": "192.2.1.3",
        "globalCredentialsId": ""
    }
    resp = requests.post(api_url, headers=headers, data=json.dumps(body))
    response_json = resp.json()


def format_dict_to_list(networkDevice):
    return [networkDevice["hostname"], networkDevice["platformId"], networkDevice["managementIpAddress"]]
