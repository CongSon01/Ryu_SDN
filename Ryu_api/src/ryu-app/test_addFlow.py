# import requests as rq

# # flow_stat = rq.get('http://localhost:8080/flow_stat/').json()
# # topology_data = rq.get('http://localhost:8080/stats/flow/').json()
# # flow_stat_df = json_normalize(flow_stat)
# # print(topology_data)

# flow_entry = '''{
#     "dpid": 1,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "priority": 65535,
#     "actions":[
#         {
#             "type":"OUTPUT",
#             "port": "CONTROLLER"
#         }
#     ],
#     "match": {
#         "dl_dst": "01:80:c2:00:00:0e",
#         "dl_type": 35020
#     },
# }'''
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))

# flow_entry = '''{
#     "dpid": 2,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "priority": 65535,
#     "actions":[
#         {
#             "type":"OUTPUT",
#             "port": "CONTROLLER"
#         }
#     ],
#     "match": {
#         "dl_dst": "01:80:c2:00:00:0e",
#         "dl_type": 35020
#     },
# }'''
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))

# flow_entry = '''{
#     "dpid": 1,
#     "priority": 32,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "actions": [{
#         "type":"OUTPUT",
#         "port": 2
#     }],
#     "match": {
#         "in_port": 1,
#         "dl_src": "42:43:a9:b5:62:58",
#         "dl_dst": "ee:36:53:04:b9:26"
#     },
# }'''

# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))

# flow_entry = '''{
#     "dpid": 1,
#     "priority": 32,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "actions": [{
#         "type":"OUTPUT",
#         "port": 1
#     }],
#     "match": {
#         "in_port": 2,
#         "dl_src": "42:43:a9:b5:62:58",
#         "dl_dst": "ee:36:53:04:b9:26"
#     },
# }'''

# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))

# flow_entry = '''{
#     "dpid": 2,
#     "priority": 32,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "actions": [{
#         "type":"OUTPUT",
#         "port": 1
#     }],
#     "match": {
#         "in_port": 2,
#         "dl_src": "42:43:a9:b5:62:58",
#         "dl_dst": "ee:36:53:04:b9:26"
#     },
# }'''

# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))

# flow_entry = '''{
#     "dpid": 2,
#     "priority": 32,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "actions": [{
#         "type":"OUTPUT",
#         "port": 2
#     }],
#     "match": {
#         "in_port": 1,
#         "dl_src": "42:43:a9:b5:62:58",
#         "dl_dst": "ee:36:53:04:b9:26"
#     },
# }'''

# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))


import requests as rq
# flow_entry = '''{
#     "dpid": 1,
#     "priority": 1,
#     "idle_timeout": 0,
#     "hard_timeout": 0,
#     "flags": 0,
#     "length": 104,
#     "actions": [{
#         "type":"OUTPUT",
#         "port": 2
#     }],
#     "match": {
#         "in_port": 1,
#         "dl_src": "2a:db:a4:83:fe:2f",
#         "dl_dst": "9e:43:6d:0e:ec:97"
#     },
#     "table_id": 0
# }'''
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'})) 

# print(rq.post('http://localhost:8080/stats/flowentry/add', data=flow_entry, headers={'Content-type': 'text/plain'}))





def addFlow( dpid, priority, inPort, outPort, dl_src, dl_dst ):
    return {
        "dpid": dpid,
        "priority": priority,
        "idle_timeout": 0,
        "hard_timeout": 0,
        "actions":[
            {
                "type":"OUTPUT",
                "port": outPort
            }
        ],
       "match": {
        "in_port": inPort,
        "dl_src": str(dl_src),
        "dl_dst": str(dl_dst)
    }}


a = "a2:65:56:d5:59:9b"
b = "9e:b9:57:76:a7:91"


# flow_entry = addFlow(7,201, 10, 1, b, a)
# print(rq.post('http://10.20.0.209:8080/s
# tats/flowentry/add', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 

def add_controller(dpid):
    return {
            "dpid": dpid,
            'len': 80,
            "actions":[
                {
                    "type":"OUTPUT",
                    "port": "CONTROLLER"
                }
            ],
        "match": {},
    }
print(rq.post('http://10.20.0.209:8080/stats/flowentry/add', data=str(add_controller(3)), headers={'Content-type': 'text/plain'})) 
print(rq.post('http://10.20.0.209:8080/stats/flowentry/add', data=str(add_controller(4)), headers={'Content-type': 'text/plain'})) 
print(rq.post('http://10.20.0.211:8080/stats/flowentry/add', data=str(add_controller(1)), headers={'Content-type': 'text/plain'})) 
print(rq.post('http://10.20.0.211:8080/stats/flowentry/add', data=str(add_controller(2)), headers={'Content-type': 'text/plain'})) 

# flow_entry = addFlow(6,100, 2, 3, b,  a)
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 
# flow_entry = addFlow(6,100,3, 2,  a, b)
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 

# flow_entry = addFlow(2,102, 1, 3, b,  a)
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 
# flow_entry = addFlow(2,102,3, 1,  a, b)
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 


# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(add_controller(1)), headers={'Content-type': 'text/plain'})) 
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(add_controller(2)), headers={'Content-type': 'text/plain'})) 
# print(rq.post('http://localhost:8080/stats/flowentry/add', data=str(add_controller(3)), headers={'Content-type': 'text/plain'})) 

