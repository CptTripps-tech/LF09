import json
import requests


def get_networkdevice(ticket_id):
    api_url = "http://localhost:58000/api/v1/network-device"

    headers = {"X-Auth-Token": ticket_id}

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Request status: ", resp.status_code)

    response_json = resp.json()
    networkdevices = response_json["response"]

    for networkDevice in networkdevices:
        if "hostname" in networkDevice:
            print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t",
                  networkDevice["managementIpAddress"])
        else:
            continue
