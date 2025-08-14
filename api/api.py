import requests


url = 'https://words.dev-apis.com/word-of-the-day?random=1'


res = requests.get(url)

data =  res.json()

print(f'Word: {data['word']}')



