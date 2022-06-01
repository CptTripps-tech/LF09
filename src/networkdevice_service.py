import json
import requests


def get_networkdevices(ticket_id):
    api_url = "http://localhost:58000/api/v1/network-device"

    headers = {"X-Auth-Token": ticket_id}

    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    networkdevices = response_json["response"]
    formatted_networkdevices = []
    for networkDevice in networkdevices:
        if "hostname" in networkDevice:
            formatted_networkdevices.append(format_dict_to_list(networkDevice))
            print(format_dict_to_list(networkDevice))
        else:
            continue
    return formatted_networkdevices


def format_dict_to_list(networkDevice):
    return [networkDevice["hostname"],  networkDevice["platformId"], networkDevice["managementIpAddress"]]
