import json
import requests

from src.networkdevice_service import get_networkdevice
from src.host_service import *
from src.ticket_service import get_ticket
from src.user_service import *

SERVICE_TICKET = 'NC-19-7661d50f182946278a7e-nbi'

# get_host(SERVICE_TICKET)
# get_networkdevice(SERVICE_TICKET)
# get_health(SERVICE_TICKET)
# get_host_by_ip(SERVICE_TICKET, '192.1.2.1')
get_users(SERVICE_TICKET)
