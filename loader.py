import requests
import json
import pandas as pd
import re
import sys

restaurant_data=pd.read_excel('/Users/sharadsharma/Downloads/tp.xlsx')

req_data_json=restaurant_data.to_json(orient='index')
data_original=req_data_json
url_original='https://sharad-hw1.firebaseio.com/vgsales.json'
resp_original_data=requests.put(url_original,data_original)