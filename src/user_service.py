import json
import requests


def get_users(ticket_id):
    api_url = "http://localhost:58000/api/v1/user"

    headers = {"X-Auth-Token": ticket_id}

    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    users = response_json["response"]
    formatted_users = []
    for user in users:
        for i in user['authorization']:
            formatted_users.append(format_dict_to_list(user, i))
            #print("Role:", i['role'])
        #print("Username:", user['username'])
        #print("Password:", user['password'])
    return formatted_users


def format_dict_to_list(user, i):
    return [i['role'], user['username'], user['password']]


def add_user(ticket_id, username, password):
    user = {
        "username": username,
        "password": password,
        "authorization": [{"role": "ROLE_ADMIN"}]
    }
    print(user)
    api_url = "http://localhost:58000/api/v1/user"

    headers = {"X-Auth-Token": ticket_id, 'Content-Type': 'application/json'}

    resp = requests.post(api_url, headers=headers, data=json.dumps(user))

    print(resp.json())
