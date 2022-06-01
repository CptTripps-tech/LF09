import json
import requests

from networkdevice_service import get_networkdevices
from host_service import *
from ticket_service import get_ticket
from user_service import *

SERVICE_TICKET = 'NC-19-7661d50f182946278a7e-nbi'

# get_hosts(SERVICE_TICKET)
# get_networkdevice(SERVICE_TICKET)
# get_host_by_ip(SERVICE_TICKET, '192.1.2.1')
get_users(SERVICE_TICKET)
