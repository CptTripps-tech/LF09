import json
import requests


def get_hosts(ticket_id):
    api_url = "http://localhost:58000/api/v1/host"

    headers = {"X-Auth-Token": "NC-19-7661d50f182946278a7e-nbi"}

    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    hosts = response_json["response"]
    formatted_hosts = []
    for host in hosts:
        if 'hostName' in host:
            formatted_host = format_dict_to_list(host)
            #print(formatted_host)
            formatted_hosts.append(formatted_host)
        else:
            continue
    return formatted_hosts


def format_dict_to_list(host):
    return [host["hostName"], host["hostIp"], host["hostMac"], host["connectedInterfaceName"]]


def get_hostcount(ticket_id):
    api_url = "http://localhost:58000/api/v1/host/count"

    headers = {"X-Auth-Token": "NC-19-7661d50f182946278a7e-nbi"}

    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    hostcount = response_json["response"]
    print("Number of hosts: ", hostcount)


def get_host_by_ip(ticket_id, ip_address):
    api_url = "http://localhost:58000/api/v1/host/ip-address/" + ip_address

    headers = {"X-Auth-Token": "NC-19-7661d50f182946278a7e-nbi"}

    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    hostname = response_json["hostName"]
    hostIp = response_json["hostIp"]
    hostType = response_json["hostType"]
    print("Hostname:", hostname)
    print("Host-IP:", hostIp)
    print("Host-Type:", hostType)
