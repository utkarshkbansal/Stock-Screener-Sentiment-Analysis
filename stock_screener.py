from finvizfinance.screener.overview import Overview
import pandas as pd
import csv
import os

def get_undervalued_stocks():
    """
    Returns a list of tickers with:
    - Positive Operating Margin
    - Debt-to-Equity ratio under 1
    - Low P/B (under 1)
    - Low P/E ratio (under 15)
    - Low PEG ratio (under 1)
    - Positive Insider Transactions
    """
    foverview = Overview()
    filters_dict = {
        'Debt/Equity': 'Under 1',
        'PEG': 'Low (<1)',
        'Operating Margin': 'Positive (>0%)',
        'P/B': 'Low (<1)',
        'P/E': 'Low (<15)',
        'InsiderTransactions': 'Positive (>0%)'
    }
    foverview.set_filter(filters_dict=filters_dict)
    df_overview = foverview.screener_view()
    if not os.path.exists('out'):
        os.makedirs('out')
    df_overview.to_csv('out/Overview.csv', index=False)
    tickers = df_overview['Ticker'].to_list()
    return tickers

if __name__ == "__main__":
    undervalued_stocks = get_undervalued_stocks()
    print(undervalued_stocks)
