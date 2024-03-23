import requests
import send_email

topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&from=2024-02-23" \
      "&sortBy=publishedAt" \
      "&apiKey=72a4645cd11f4b0baff0e433cca52643" \
      "&language=en"
api_key = "72a4645cd11f4b0baff0e433cca52643"

#temp = f"{index+1}: {article['title']}\n{article['description']}\n\n"
request = requests.get(url)
content = request.json()
body = "Subject: Today's News" + "\n"

for index, article in enumerate(content["articles"]):
    if article["title"] is not None:
        body = body + str(index + 1) + " Title:" + article['title'] + "\n" + "Description:" \
               + article['description'] \
               + "\n" + article["url"] + 2*"\n"
        #body = body + f"{index+1}: {article['title']}\n{article['description']} \n\n"
body = body.encode("utf-8")

send_email.sendemail("cap8.chirag@gmail.com", body)
