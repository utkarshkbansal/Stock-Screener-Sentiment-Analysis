from finvizfinance.screener.overview import Overview
import pandas as pd
import os
import matplotlib.pyplot as plt

def get_undervalued_stocks():
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

def visualize_overview_data():
    df = pd.read_csv('out/Overview.csv')
    # Example visualization: Distribution of stocks by sector
    sector_counts = df['Sector'].value_counts()
    plt.figure(figsize=(10, 5))
    sector_counts.plot(kind='bar')
    plt.title('Distribution of Stocks by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Number of Stocks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    undervalued_stocks = get_undervalued_stocks()
    print(undervalued_stocks)
    visualize_overview_data()
