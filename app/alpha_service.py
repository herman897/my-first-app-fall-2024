import os

from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line


load_dotenv() # looks in the ".env" file for env vars

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
