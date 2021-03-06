import requests


def get_api(ticket_id):
    api_url = "http://localhost:58000/api/v1/user"
    headers = {"X-Auth-Token": ticket_id}
    return requests.get(api_url, headers=headers, verify=False)


def post_api(ticket_id, data):
    api_url = "http://localhost:58000/api/v1/user"
    headers = {"X-Auth-Token": ticket_id, 'Content-Type': 'application/json'}
    return requests.post(api_url, headers=headers, data=data)


def get_users(ticket_id):
    resp = get_api(ticket_id)
    print("Request status: ", resp.status_code)

    response_json = resp.json()
    users = response_json["response"]
    formatted_users = []
    for user in users:
        for i in user['authorization']:
            formatted_users.append(format_dict_to_list(user, i))
            # print("Role:", i['role'])
        # print("Username:", user['username'])
        # print("Password:", user['password'])
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

    resp = post_api(ticket_id, data=json.dumps(user))

    print(resp.json())
