# YT Video: https://www.youtube.com/watch?v=PuZY9q-aKLw&t=957s&ab_channel=NeuralNine
# Imports for our Projects

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import requests
import urllib.request
from bs4 import BeautifulSoup

from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

def Pull_Data():
        #URL of AAPL stock
    url = 'https://finance.yahoo.com/quote/AAPL/'

        #Connect to the URL
    response = requests.get(url)

    #Parse HTML and save to BeautifulSoup Object
    soup = BeautifulSoup(response.text, "html.parser")
    
    #We are scanning specifically for the stock price to generate a predicition for the future
    line_count = 1 #to track where we are
    for one_a_tag in soup.findAll('a'):
       #Need someone to identify the specific lines for the pricing of the stock. I am not fluent in HTML -Daniel/AKA Xexvis




def print_hi(from_dimitri):
    print(f'Hi, {from_dimitri}')


if __name__ == '__main__':
    print_hi("Whats up CS Club!  Howdy, boys.  Lets get Rowdy.")
