import json

import requests

ip = "https://management.azure.com/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/networkInterfaces/TestNetInterfaceB?api-version=2022-05-01"
headers = {"Content-Type": "application/json",
           "Authorization": ""}
body = {
    "properties": {
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "properties": {
                    "publicIPAddress": {
                        "id": "/subscriptions/5faca297-4fe2-4138-89f2-c852ef0b364e/resourceGroups/pis_group/providers/Microsoft.Network/publicIPAddresses/test-ip"
                    },
                    "subnet": {
                        "id": "/subscriptions/f5d942d0-c01b-410b-ba53-5c9fa384a82f/resourceGroups/CloudComputing/providers/Microsoft.Network/virtualNetworks/CloudCompVN2/subnets/default"
                    }
                }
            }
        ]
    },
    "location": "westeurope"
}

query = requests.put(ip,data=json.dumps(body),headers=headers)


print(query.status_code)
print(query.text)