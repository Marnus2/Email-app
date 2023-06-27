import requests
from send_email import send_email

api_key= "df98110844c348c29494244b01ccbad3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-27&sortBy=publishedAt&apiKey=df98110844c348c29494244b01ccbad3"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

send_email(message=body)