from transformers import pipeline
import yfinance as yf
from goose3 import Goose
from requests import get
import pandas as pd
import os

def get_ticker_news_sentiment(ticker):
    """
    Returns a Pandas dataframe of the given ticker's most recent news article headlines,
    with the overall sentiment of each article.

    Args:
        ticker (string)

    Returns:
        pd.DataFrame: {'Date', 'Article title', 'Article sentiment'}
    """
    ticker_news = yf.Ticker(ticker)
    news_list = ticker_news.get_news()
    extractor = Goose()
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    data = []
    for dic in news_list:
        title = dic['title']
        response = get(dic['link'])
        article = extractor.extract(raw_html=response.content)
        text = article.cleaned_text
        date = article.publish_date
        if len(text) > 512:
            data.append({'Date': f'{date}', 'Article title': f'{title}', 'Article sentiment': 'NaN too long'})
        else:
            results = pipe(text)
            data.append({'Date': f'{date}', 'Article title': f'{title}', 'Article sentiment': results[0]['label']})
    df = pd.DataFrame(data)
    return df

def generate_csv(ticker):
    df = get_ticker_news_sentiment(ticker)
    if not os.path.exists('out'):
        os.makedirs('out')
    df.to_csv(f'out/{ticker}.csv', index=False)

if __name__ == "__main__":
    from stock_screener import get_undervalued_stocks
    undervalued_stocks = get_undervalued_stocks()
    for ticker in undervalued_stocks:
        generate_csv(ticker)
