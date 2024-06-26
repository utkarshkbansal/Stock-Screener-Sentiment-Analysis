from transformers import pipeline
import yfinance as yf
from goose3 import Goose
from requests import get
import pandas as pd
import os
import matplotlib.pyplot as plt

def get_ticker_news_sentiment(ticker):
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

def plot_sentiment_distribution(ticker, df):
    sentiment_counts = df['Article sentiment'].value_counts()
    plt.figure(figsize=(10, 5))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title(f'Sentiment Distribution for {ticker}')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def generate_csv(ticker):
    df = get_ticker_news_sentiment(ticker)
    if not os.path.exists('out'):
        os.makedirs('out')
    df.to_csv(f'out/{ticker}.csv', index=False)
    plot_sentiment_distribution(ticker, df)

if __name__ == "__main__":
    from stock_screener import get_undervalued_stocks
    undervalued_stocks = get_undervalued_stocks()
    for ticker in undervalued_stocks:
        generate_csv(ticker)
