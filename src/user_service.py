import json
import requests


def get_users(ticket_id):
    api_url = "http://localhost:58000/api/v1/user"

    headers = {"X-Auth-Token": ticket_id}

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Request status: ", resp.status_code)

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
