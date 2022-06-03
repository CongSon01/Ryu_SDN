


import requests as rq

# def addFlow( dpid, priority, inPort, outPort, dl_src, dl_dst ):
#     return {
#         "dpid": dpid,
#         "priority": priority,
#         "idle_timeout": 0,
#         "hard_timeout": 0,
#         "actions":[
#             {
#                 "type":"OUTPUT",
#                 "port": outPort
#             }
#         ],
#        "match": {
#         "in_port": inPort,
#         "dl_src": str(dl_src),
#         "dl_dst": str(dl_dst)
#     }}

# a = "5a:71:18:4f:85:21"
# b = "62:1a:c6:93:c1:a7"
# flow_entry = addFlow(1,1, 2, 1, b, a)
# print(rq.post('http://localhost:8080/stats/flowentry/delete_strict', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 

# flow_entry = addFlow(1,1, 1, 2, a,  b)
# print(rq.post('http://localhost:8080/stats/flowentry/delete_strict', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 

# flow_entry = addFlow(2,32, 1, 2, b,  a)
# print(rq.post('http://localhost:8080/stats/flowentry/delete_strict', data=str(flow_entry), headers={'Content-type': 'text/plain'})) 

# flow_entry = addFlow(2,32,2, 1,  a, b)
print(rq.delete('http://localhost:8080/stats/flowentry/clear/1', headers={'Content-type': 'text/plain'}))
print(rq.delete('http://localhost:8080/stats/flowentry/clear/2', headers={'Content-type': 'text/plain'}))
print(rq.delete('http://localhost:8080/stats/flowentry/clear/3', headers={'Content-type': 'text/plain'}))
print(rq.delete('http://localhost:8080/stats/flowentry/clear/4', headers={'Content-type': 'text/plain'}))




