import requests
import pandas as pd
import json
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import date,timedelta
from flask import Flask, jsonify, request, send_file
from pymongo import MongoClient
from flask_restful import Api, Resource
import io

app = Flask(__name__)

#Connect to MongoDB and create db and collection
client = MongoClient("mongodb://db:27017")
db = client.BTCDB
btcprice = db["btcprice"]

#Get the dates
today = date.today()
today = today.strftime("%Y-%m-%d")

yesterday = date.today()-timedelta(1)
yesterday = yesterday.strftime("%Y-%m-%d")

month = date.today()-timedelta(30)
month = month.strftime("%Y-%m-%d")

#load data for the required dates
df = data.DataReader("BTC-USD",
                       start=month,
                       end=today,
                       data_source='yahoo')  #['Adj Close']
df['Close'].plot()

plt.title('BTC Price Chart')
plt.ylabel('Price in $USD')
plt.xlabel('Dates')
plt.grid(which="major", linestyle='-.', linewidth=0.5)

bytes_image = io.BytesIO()
plt.savefig(bytes_image, format='png')
bytes_image.seek(0)

df.reset_index(inplace=True)

# #Calculate the percenatges diff of the price
# daily_var = round(100*(df[df['Date']==today]['Close'] - df[df['Date'] == today]['Open'])/df[df['Date'] == today]['Close'], 2)

#convert df to json
#json_data = df.to_json(orient="records", date_format='iso')
dict_data = df.to_dict(orient='records')

#Insert data to MongoDB
#x =btcprice.insert_many(json_data)
x =btcprice.insert_many(dict_data)



@app.route('/')
def info():
    return('Daily Bitcoin Price Volatility Calculator')


@app.route('/daily', methods=["GET", "POST"])
def daily():
    #Calculate the percenatges diff of the price
    daily_var = round(100*(df[df['Date']==today]['Close'] - df[df['Date'] == today]['Open'])/df[df['Date'] == today]['Close'], 2)

    retJson = {
        "Current Bitcoin Price": df[df['Date'] == today]['Close'].values[0],
        "Today Volatility": daily_var.values[0]
    }
    return jsonify(retJson)

@app.route('/statistics', methods=["GET", "POST"])
def month_stats():
    #Calculate the max price
    
    m_date = df[df['High'] == max(df['High'])]['Date'].values[0]
    max_date = pd.to_datetime(str(m_date)).strftime("%Y-%m-%d")

    #Calculate the min price
    
    m_date = df[df['Low'] == max(df['Low'])]['Date'].values[0]
    min_date = pd.to_datetime(str(m_date)).strftime("%Y-%m-%d")

    retJson = [
        {"Date": max_date,
        "Highest Price of Last 30 Days": max(df['High'])},
        {"Date": min_date,
        "Lowest Price of Last 30 Days": min(df['Low'])}
    ]
    return jsonify(retJson)

@app.route('/monthly')
def monthly():
    return send_file(bytes_image,
                    attachment_filename='bytes_image.png',
                    mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
