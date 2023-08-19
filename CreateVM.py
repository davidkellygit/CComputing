import json

import requests

ip = "https://management.azure.com/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Compute/virtualMachines/TestVMB?api-version=2022-08-01"
headers = {"Content-Type": "application/json",
           "Authorization": ""}
body = {
    "name": "CloudComp2",
    "location": "westeurope",
    "properties": {
        "osProfile": {
            "adminUsername": "David",
            "adminPassword": "HelloWorld12345",
            "secrets": [

            ],
            "computerName": "myVM",
            "linuxConfiguration": {
                "disablePasswordAuthentication": false
            }
        },
        "networkProfile": {
            "networkInterfaces": [
                {
                    "id": "/subscriptions/f5d942d0-c01b-410b-ba53-5c9fa384a82f/resourceGroups/CloudComputing/providers/Microsoft.Network/networkInterfaces/CloudCompVN2"
                }
            ]
        },
        "storageProfile": {
            "imageReference": {
                "sku": "16.04-LTS",
                "publisher": "Canonical",
                "version": "latest",
                "offer": "UbuntuServer"
            },
            "dataDisks": [

            ]
        },
	"hardwareProfile": {
                "vmSize": "Standard_D1_v2"
	 }
    }
}

query = requests.put(ip,data=json.dumps(body),headers=headers)

print(query.status_code)
print(query.text)