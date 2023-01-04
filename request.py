import http.client

conn = http.client.HTTPConnection("localhost")

payload = "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"user.login\",\n    \"params\": {\n        \"user\": \"Admin\",\n        \"password\": \"zabbix\"\n    },\n    \"id\": 1,\n    \"auth\": null\n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/api_jsonrpc.php", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
