import apizabbix

api = apizabbix.connect()

hostgroups = api.hostgroup.get()

from pprint import pprint
pprint(hostgroups)

api.user.logout()