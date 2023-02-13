import requests

url = "https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0"
headers = {"User-Agent":"Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open('wanted.html', 'w', encoding='utf8') as f:
    f.write(res.text)