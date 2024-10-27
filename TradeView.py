from ast import Try
import yfinance as yfn
import math
import pandas as pd
import time


def main():
    tickers = ["BA"]
    WatchPrice(tickers, 140, 160) 
    #Add whatever you want to check for


def WatchPrice(tickerStr, lowThreshold, highThreshold):
    try:
        ticker = yfn.Ticker(tickerStr)
        output = "0"
        currentPrice = ticker.info["currentPrice"]
        if currentPrice >= highThreshold:
            output = "high price"
        elif currentPrice <= lowThreshold:
            output = "low price"
        else:
            output = "in bound of limits"
    except:
        output = "-1"
    return {"output" : output, "curPrice" : currentPrice}

def AtLow(tickers, threshold):
    for tickerStr in tickers:
        try:
            ticker = yfn.Ticker(tickerStr)
            dailyLows = ticker.history(period="12mo").loc[:, ["Low"]]
            minValue = math.inf
            for row in dailyLows.iterrows():
                if row[1][0] < minValue:
                    minValue = row[1][0]
            currentPrice = ticker.info["currentPrice"]
            currentPriceToLow = minValue / currentPrice
            if  currentPriceToLow >= threshold:
                print("low low")
        except:
            print("error")

def AtHigh(tickers, threshold):
    for tickerStr in tickers:
        try:
            ticker = yfn.Ticker(tickerStr)
            dailyHighs = ticker.history(period="12mo").loc[:, ["High"]]
            maxValue = 0
            for row in dailyHighs.iterrows():
                if row[1][0] > maxValue:
                    maxValue = row[1][0]
            currentPrice = ticker.info["currentPrice"]
            currentPriceToHigh =  currentPrice / maxValue
            if currentPriceToHigh >= threshold:
                print("high high")
        except:
            print("error")

def IntervalIncrease(tickerStr, days, threshold):
    if days > 365:
        print("too many days")
    else:
        try:
            ticker = yfn.Ticker(tickerStr)
            daysIndx = ticker.history(period="12mo").index[days-1]
            firstDayPrice = ticker.history(period="12mo").at[daysIndx, "Open"]
            currentPrice = ticker.info["currentPrice"]
            increase = 1 - (firstDayPrice / currentPrice)
            if increase >= threshold:
                print(increase)
        except:
            print("error")

def IntervalDecrease(tickers, days, threshold):
    if days > 365:
        print("too many days")
    else:
        for tickerStr in tickers:
            try:
                ticker = yfn.Ticker(tickerStr)
                daysIndx = ticker.history(period="12mo").index[days-1]
                firstDayPrice = ticker.history(period="12mo").at[daysIndx, "Open"]
                currentPrice = ticker.info["currentPrice"]
                decrease = 1 - (currentPrice / firstDayPrice)
                if decrease >= threshold:
                    print("high decrease")
            except:
                print("error")   