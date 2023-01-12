from pyzabbix.api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/api_jsonrpc.php")
zapi.login("Admin", "zabbix")

print("Versão da API do Zabbix: ", zapi.api_version())

#teste