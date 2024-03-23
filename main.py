import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-23" \
      "&sortBy=publishedAt" \
      "&apiKey=72a4645cd11f4b0baff0e433cca52643"
api_key = "72a4645cd11f4b0baff0e433cca52643"

request = requests.get(url)
content = request.json()

for index, article in enumerate(content["articles"]):
    print(f"{index}: {article['title']}: {article['description']}")
