# La centrale annonce

import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = [[1458817125,2015,150,6,110500,5,0,1458777600,41190,1459993610,30,0,1,0,0,0,0,0,0,0,0,0,0,0,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print("test")
print(r, r.text)


# https://www.lacentrale.fr/auto-occasion-annonce-69108653033.html
# Price return : 21 092.49
# Real price : 18 990 
# Gap is important but the 3 dates couldn't been convert properly and the postal code is in fact in the wrong country