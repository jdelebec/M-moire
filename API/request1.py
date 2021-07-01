import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = [[1458817125,2011,190,6,125000,5,1,1458777600,66954,1459993610,14,0,1,0,0,0,0,0,0,0,0,0,0,0,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print("test")
print(r, r.text)


# Return 18653.02 and the real price is 18300