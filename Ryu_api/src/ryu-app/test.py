import requests as rq
switches = rq.get('http://localhost:8080/topology_data').json()['switch']
devices = [{"id": "of:" + str(switch['dpid']), "type":"SWITCH"} for switch in switches]

hosts = rq.get('http://localhost:8080/topology_data').json()['host']
hosts = [{"mac":str(host['mac']) ,
         "ipAddresses": [str(host['ipv4'][0])],
         "locations": [
             {"elementId":"of:" + str(host['port']['dpid'])},
             {"port": int(host['port']['name'].split("eth")[1])}
             ]} for host in hosts if host['ipv4'] != []]

links = rq.get('http://localhost:8080/topology_data').json()['link']
links = [{"src": {"port": int(link["src"]["name"].split("eth")[1]), "id":"of:" + str(link['src']['dpid']) },
            "dst": {"port": int(link["dst"]["name"].split("eth")[1]), "id":"of:" + str(link['dst']['dpid']) }} for link in links]

print(hosts)
