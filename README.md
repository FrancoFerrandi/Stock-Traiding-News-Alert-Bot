# Stock Trading News Alert Bot

## Description

This bot is designed to perform the following tasks automatically:

1. Retrieve the stock price of a specific company (e.g., Tesla Inc.) using the Alpha Vantage API.

2. Calculate the percentage change between the previous day's closing price and the day before.

3. If the change is significant (≥ 5%), fetch relevant news about the company using the NewsAPI.

4. Format the news headlines and send them via SMS using Twilio.

## Technologies Used

**Python:** Main language of the project.

**Requests:** For making HTTP requests to the APIs.

**Twilio:** For sending SMS messages.

**Python-dotenv:** To load environment variables from a .env file.

## Prerequisites

1. **API Keys:**

    - Alpha Vantage: To fetch stock data.

    - NewsAPI: To fetch relevant news.

    - Twilio: To send SMS messages.

2. **Environment Setup:**

    - Python 3.8 or higher.

    - .env file with the following variables:
    ```
    STOCK_API_KEY=your_alpha_vantage_api_key
    NEWS_API_KEY=your_news_api_key
    VIRTUAL_TWILIO_NUMBER=your_twilio_virtual_number
    VERIFIED_NUMBER=your_verified_phone_number
    TWILIO_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    ```

## Installation and Setup

1. **Clone the repository:**
```
git clone https://github.com/FrancoFerrandi/Stock-Traiding-News-Alert-Bot.git
cd Stock-Traiding-News-Alert-Bot
```

2. **Create the .env file:**

Create a .env file in the root directory and add the variables listed above.

3. **Install dependencies:**
```
pip install -r requirements.txt
```

## Execution

Run the bot with:
```
python main.py
```

## Main Functions

### `validate_env_variables`

Validates that all required environment variables are set. If any are missing, the program terminates with an error message.

### `fetch_stock_data`
Fetches daily stock data from Alpha Vantage.

### `calculate_price_difference`

Calculates the price difference and percentage change between two consecutive days.

### `fetch_news`

Fetches up to three relevant news articles about the company from NewsAPI.

### `format_articles`

Formats the news into messages ready to send via SMS.

### `send_messages`

Sends the formatted messages using Twilio.

## Example Output

If Tesla's stock price changes significantly, the bot might send a message like:

TSLA: 🔺5%
Headline: Tesla reaches a new all-time high
Brief: Tesla stock surges after announcing a new electric vehicle model.

## Notes

- Ensure you have enough credit in Twilio to send SMS messages.

- API keys have usage limits. Refer to the Alpha Vantage and NewsAPI documentation for more information.
