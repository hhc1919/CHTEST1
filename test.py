from falconpy import Hosts
import json

falcon = Hosts(client_id = "da159257d7e7450a99eed80604e7957f", client_secret = "pmtgQAsbxhEcMkwJq2a934CZF758OoYIjB6vN1K0")
response = falcon.query_devices_by_filter(offset=1,
                                          limit=5000,
                                          sort="hostname.asc",
                                          filter="tags:'FalconGroupingTags/USB-Allow'"
                                          )
list = response['body']['resources']
hostname_list = falcon.get_device_details(ids=list)
hostnames = hostname_list['body']['resources']
h = json.dumps(hostnames, indent=4)
#print(h)

hosts = []
for item in hostnames:
    hosts.append(item['hostname'])
print(len(hosts))
print(hosts)