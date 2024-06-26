# Stock Screener & Sentiment Analysis

This project includes a Python-based stock screener and AI-based sentiment analysis tool to identify undervalued stocks and analyze their sentiment using financial news articles. It uses the `finvizfinance` library for stock screening and the `transformers` library with a pre-trained FinBERT model for sentiment analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Windows/MacOS/Linux machine
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/stock-screener-sentiment-analysis.git
   cd stock-screener-sentiment-analysis
2. **Create a virtual environment**
   ```sh
    python -m venv venv
   ```
3. **Activate the virtual environment based on your machine**
   ```sh
    source venv/bin/activate   # On macOS/Linux
   ```
   ```sh
    .\venv\Scripts\activate    # On Windows
   ```
4. **Install the dependencies**
    ```sh
    - pip install -r requirements.txt
    ```
### Usage

**Run the stock screener script:**
  ```sh
  python stock_screener.py
  ```
   - This will generate an **Overview.csv** file in the **out** directory with the tickers of undervalued stocks.

**Run the sentiment analysis script:**
  ```sh
  python sentiment_analysis.py
  ```
   - This will generate individual CSV files for each ticker in the **out** directory, containing news article titles and their sentiment analysis.



### LICENSE

```markdown
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

