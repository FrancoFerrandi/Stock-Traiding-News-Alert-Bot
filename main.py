import os
from functions import validate_env_variables, fetch_stock_data, calculate_price_difference, fetch_news, format_articles, send_messages

# Validate environment variables
required_vars = [
    "STOCK_API_KEY", "NEWS_API_KEY", "VIRTUAL_TWILIO_NUMBER", 
    "VERIFIED_NUMBER", "TWILIO_SID", "TWILIO_AUTH_TOKEN"
]

validate_env_variables(*required_vars)

# Load environment variables

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
VIRTUAL_TWILIO_NUMBER = os.getenv("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.getenv("VERIFIED_NUMBER")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Fetch stock data and calculate changes

stock_data = fetch_stock_data(STOCK_NAME, STOCK_API_KEY)
difference, diff_percent, direction = calculate_price_difference(stock_data)

# Fetch news if the percentage change is significant

if abs(diff_percent) >= 5:
    articles = fetch_news(COMPANY_NAME, NEWS_API_KEY)
    if not articles:
        print("No news articles found.")
        exit()

    # Format and send news messages
    messages = format_articles(STOCK_NAME, direction, diff_percent, articles)
    send_messages(messages, TWILIO_SID, TWILIO_AUTH_TOKEN, VIRTUAL_TWILIO_NUMBER, VERIFIED_NUMBER)