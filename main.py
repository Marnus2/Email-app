import requests

api_key= "df98110844c348c29494244b01ccbad3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-26&sortBy=publishedAt&apiKey=df98110844c348c29494244b01ccbad3"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
        print(article["title"])
        print(article["description"])