import json
import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '35ea63b0ed1e8e8bc29bacf9a9ccfe14'
redirect_uri = 'https://naver.com'
authorize_code = 'DfUXakhpViYoLPWnxY0ciB45AHW3nshi0KKxY_E5Jkm2PsYzScQ1Cnt10sNLgCBmRBvt5Ao9dNsAAAF-T4xR6w'

data = {
    'grant_type': 'authorization_code',
    'client_id': rest_api_key,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
}

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장

with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)
