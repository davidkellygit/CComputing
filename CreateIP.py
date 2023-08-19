import json

import requests

ip = "https://management.azure.com/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/publicIPAddresses/TestIPAddressB?api-version=2022-05-01"
headers = {"Content-Type": "application/json",
           "Authorization": ""}
body = {
    "properties": {
        "publicIPAllocationMethod": "Static",
        "idleTimeoutInMinutes": 10,
        "publicIPAddressVersion": "IPv4"
    },
    "sku": {
        "name": "Basic"
    },
    "location": "westeurope"
}

query = requests.put(ip,data=json.dumps(body),headers=headers)

print(query.status_code)
print(query.text)