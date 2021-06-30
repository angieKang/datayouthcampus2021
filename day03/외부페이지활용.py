import requests
import json

url = "https://dapi.kakao.com/v2/local/search/address.json"
apikey = "3aadf67508eaeff23212afa19abd14ff"
headers = {"Authorization": "KakaoAK "+ apikey}
parameters = {"query": "경기 광명시 철산로 57"}

response = requests.get(url, headers=headers, params=parameters)
print(response)    #http response code 200: success
print(response.text)
jsonResponse = json.loads(response.text)
print(jsonResponse)
print(json.dumps(jsonResponse, indent=4, ensure_ascii=False))


