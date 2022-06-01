import json
import requests


def get_ticket():
    API_URL = "http://localhost:58000/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }

    body_json = {
        "username": "cisco",
        "password": "cisco123!"
    }

    resp = requests.post(API_URL, json.dumps(body_json), headers=headers, verify=False)

    print("Ticket request status: ", resp.status_code)
    response_json = resp.json()

    serviceTicket = response_json["response"]["serviceTicket"]
    print("The service ticket number is: ", serviceTicket)
