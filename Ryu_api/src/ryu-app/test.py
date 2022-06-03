# import requests as rq
# switches = rq.get('http://localhost:8080/topology_data').json()['switch']
# devices = [{"id": "of:" + str(switch['dpid']), "type":"SWITCH"} for switch in switches]

# hosts = rq.get('http://localhost:8080/topology_data').json()['host']
# hosts = [{"mac":str(host['mac']) ,
#          "ipAddresses": [str(host['ipv4'][0])],
#          "locations": [
#              {"elementId":"of:" + str(host['port']['dpid'])},
#              {"port": int(host['port']['name'].split("eth")[1])}
#              ]} for host in hosts if host['ipv4'] != []]

# links = rq.get('http://localhost:8080/topology_data').json()['link']
# links = [{"src": {"port": int(link["src"]["name"].split("eth")[1]), "id":"of:" + str(link['src']['dpid']) },
#             "dst": {"port": int(link["dst"]["name"].split("eth")[1]), "id":"of:" + str(link['dst']['dpid']) }} for link in links]

# print(hosts)
def convert_name_switch( int_switch):
        """
            convert name int => hex
        """
        my_str = '0'
        comp1 = 'of:'
        number_zero = 16
        comp2_int = int(int_switch)
        comp2_hex = hex(comp2_int).replace('x','0')

        number_zero = comp1 + my_str.zfill( number_zero - len(str(comp2_hex))) + comp2_hex

        return number_zero

print(convert_name_switch(10))