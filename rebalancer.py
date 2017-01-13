import pandas as pd
import numpy as np

# Define portfolio and weights
target = [[22739,0.35], #VTI - total stock
          [34385,0.17], #VEA - developed
          [27102,0.14], #VWO - emerging
          [28364,0.06], #VIG - dividend
          [19655,0.05], #XLE - energy sector
          [34648,0.23]] #MUNI - municipal bonds

# Initialize portfolio dataframe
dfptf = pd.DataFrame(target,columns=["Security","Target"])
dfptf["LastPrice"] = [170.,80.,82.,32.,26.,45]
dfptf["Amount"] = 0.0
dfptf["Value"] = 0.0
dfptf["CurrentWeight"] = 0.0
dfptf["TradeWeight"] = 0.0
dfptf["TradeAmount"] = 0.0
dfptf["TradeValue"] = 0.0
dfptf["CapitalGain"] = 0.0

my_cash = 100000

# Simplified version
dfptf.TradeWeight = dfptf.Target
dfptf.TradeAmount = np.floor(dfptf.TradeWeight*my_cash/dfptf.LastPrice)
dfptf.TradeValue = dfptf.TradeAmount * dfptf.LastPrice

# Update
dfptf.Amount = dfptf.TradeAmount
dfptf.Value = dfptf.TradeValue


def rebalancer(amount):
	toInvest = amount+my_cash-dfptf.Value.sum()

	# New price
	dfptf["LastPrice"] = [120.,150.,86.,54.,40.,42.]

	dfptf.CurrentWeight = dfptf.Value/(dfptf.Value.sum()+toInvest)
	dfptf.TradeWeight = dfptf.Target-dfptf.CurrentWeight
	dfptf.TradeAmount = np.floor(dfptf.TradeWeight*\
    	(dfptf.Value.sum()+toInvest)/dfptf.LastPrice)
	dfptf.TradeValue = dfptf.TradeAmount * dfptf.LastPrice

rebalancer(20000)