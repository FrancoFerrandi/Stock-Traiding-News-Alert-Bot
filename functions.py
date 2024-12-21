import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

def load_env_variables() -> None:
    """Cargar las variables de entorno desde el archivo .env."""
    load_dotenv()

def validate_env_variables(*variables: str) -> None:
    """Validate that all required environment variables are defined."""
    missing = [var for var in variables if not os.getenv(var)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        exit(1)

def fetch_stock_data(stock_symbol: str, api_key: str) -> dict:
    """Fetch stock data from Alpha Vantage."""
    endpoint = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": api_key,
    }
    response = requests.get(endpoint, params=params)
    if response.status_code != 200 or "Time Series (Daily)" not in response.json():
        print("Error fetching stock data.")
        print(response.json())
        exit()
    return response.json()["Time Series (Daily)"]

def calculate_price_difference(data: dict) -> (float):
    """Calculate the difference and percentage change between yesterday and the day before."""
    data_list = [value for key, value in data.items()]
    yesterday_closing = float(data_list[0]["4. close"])
    day_before_closing = float(data_list[1]["4. close"])

    difference = yesterday_closing - day_before_closing
    percentage_change = round((difference / day_before_closing) * 100)
    direction = "🔺" if difference > 0 else "🔻"
    return difference, percentage_change, direction

def fetch_news(company_name: str, api_key: str) -> list:
    """Fetch news articles related to the company."""
    endpoint = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": api_key,
        "qInTitle": company_name,
    }
    response = requests.get(endpoint, params=params)
    if response.status_code != 200:
        print("Error fetching news.")
        exit()
    articles = response.json().get("articles", [])
    return articles[:3]

def format_articles(stock_name: str, change: str, percent: int, articles: list) -> list:
    """Format articles into messages."""
    return [
        f"{stock_name}: {change}{percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

def send_messages(messages: list, twilio_sid: str, twilio_auth_token: str, from_number: str, to_number: str) -> None:
    """Send messages using Twilio."""
    client = Client(twilio_sid, twilio_auth_token)
    for message in messages:
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number,
        )
    print("Messages sent.")