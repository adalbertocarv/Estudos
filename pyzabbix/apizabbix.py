from pyzabbix import ZabbixAPI

# Create ZabbixAPI class instance
#zapi = ZabbixAPI(url='http://localhost/zabbix', user='admin', password='zabbix')


ZABBIX_SERVER = 'http://localhost/zabbix.php?action=dashboard.view'
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('admin', 'zabbix')

# Get all disabled hosts
result = zapi.host.get(status=1)
hostnames = [host['host'] for host in result1]