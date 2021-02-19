import requests, os
from twilio.rest import Client
from newsapi import NewsApiClient
import datetime

# stock info
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# end point info
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# tokens + keys
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
ALPHA_VANTAGE_KEY=os.environ.get("ALPHA_VANTAGE_KEY")
auth_sid = os.environ.get("TW_AUTH_SID")
auth_token = os.environ.get("TW_AUTH_TOKEN")
# trial_num = your trial num here
# dest_num = your dest num here

# dates from datetime
YESTERDAY = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("20%y-%m-%d")
DAY_BEFORE_YEST =(datetime.datetime.now() - datetime.timedelta(days = 2)).strftime("20%y-%m-%d")

# params
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_KEY,
}
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
tesla_data = stock_response.json()['Time Series (Daily)']
# Get yesterday and day before closing stock price
yesterday_tesla = float(tesla_data[YESTERDAY]['4. close'])
day_before_yest_tesla = float(tesla_data[DAY_BEFORE_YEST]['4. close'])
# find positive difference between closing stocks
difference = yesterday_tesla-day_before_yest_tesla
abs_diff = abs(difference)
# create object to determine if up or down
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round(((abs_diff / yesterday_tesla) * 100),2)
# if greater than 5%, get the first 3 news pieces for the COMPANY_NAME.
if diff_percent > 5:
    news_params = {
    "apiKey" : NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # Send a separate message with each article's title and description to your phone number.
    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief{article['description']}" for article in three_articles]
    client = Client(auth_sid, auth_token)
    for _ in formatted_articles:
        message = client.messages \
            .create(
            body=_,
            from_=trial_num,
            to=dest_num
            )
        #print(_)
