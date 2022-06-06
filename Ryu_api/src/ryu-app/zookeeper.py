import time

from requests import request
import requests
time_start = time.time()
while True:
    time_current = time.time()
    if time_current - time_start > 3:
        try:
            data = requests.get('http://0.0.0.0:8080/link_quality')
            requests.post('http://10.20.0.209:5000/write_data_ryu/', data=data.text)
        except: 
            print("CHUA BAT FLASK")
        time_start = time_current
    