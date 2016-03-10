# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/   
# The code for tutorial, pop_up message, and StartPage is from Youtube tutorial by https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from matplotlib import style
import urllib
import pandas as pd
import numpy as np
import Quandl

import matplotlib.colors as colors
import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.mlab as mlab
import matplotlib.font_manager as font_manager

from matplotlib import pyplot as plt

#initialize global variables
style.use('ggplot')

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

f = plt.figure()
a = f.add_subplot(111)

stock = "S&P500"
SMA_short_periods = 5;
SMA_long_periods = 5;
EMA_short_periods = 5;
EMA_long_periods = 5;

#EFFECTS: Change stock varaible to what
def changeStock(what):
    global stock
    stock = what

#EFFECTS: Change SMA Short period to what
def change_Short_SMA(what):
    global SMA_short_periods
    SMA_short_periods = what

#EFFECTS: Change SMA Long period to what
def change_Long_SMA(what):
    global SMA_long_periods
    SMA_long_periods = what

#EFFECTS: Change EMA Short period to what
def change_Short_EMA(what):
    global EMA_short_periods
    EMA_short_periods = what

#EFFECTS: Change EMA Long period to what
def change_Long_EMA(what):
    global EMA_long_periods
    EMA_long_periods = what



#EFFECTS : Tutorial Page 
def tutorial():
    def leavemini(what):
       what.destroy()

    def page2():
        leavemini(tut)
        tut2 = tk.Tk()
        def leavemini2(what):
           what.destroy()
           
        def page3():

            leavemini2(tut2)
            tut3 = tk.Tk()
            tut3.wm_title("What is SMA?")
    
            label = ttk.Label(tut3, text="What is SMA?", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text = "Thank you", command = tut3.destroy)
            B1.pack()
            tut3.mainloop()
            
        tut2.wm_title("What is EMA?")
        label = ttk.Label(tut2, text="hat is EMA?", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text = "What is SMA?", command = page3)
        B1.pack()

        tut.mainloop()
        
    tut = tk.Tk()
    tut.wm_title("What is EMA and SMA?")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(tut, text = "Tell me about EMA and SMA", command = page2)
    B1.pack()

    tut.mainloop()

#EFFECTS: Calculate Five Day Average SMA
#Simple Moving Average Period = 5days
def fivedayaverage(what):
    numEntries = len(what["Open"]) #end of entry number
    startPoint = 0
    average = 0 
    count = 0
    sum = 0
    period = 5
    #we know that the very frist 5 values do not matter, give them their value
    while (count < period):
        sum = sum + what["Close"][startPoint + count]
        what["5daySMA"][startPoint+count] = what["Close"][startPoint + count]
        count = count + 1
    #first average, and now index is 5
    average = sum / period
    what["5daySMA"][startPoint + count] = average #index is five, and first SMA period 5 
    startPoint = startPoint + 1
    while (startPoint < numEntries - period):
        #need to update the sum
        sum = 0
        count = 0
        while (count < period):
            sum = sum + what["Close"][startPoint + count]
            count = count + 1
        #end of the second while loop, update the SMA5
        average = sum / period
        what["5daySMA"][startPoint + count] = average
        startPoint = startPoint + 1

#EFFECTS: Calculate Ten Day Average SMA
def tendayaverage(what):
    numEntries = len(what["Open"]) #end of entry number
    startPoint = 0
    average = 0 
    count = 0
    sum = 0
    period = 10
    #we know that the very frist 5 values do not matter, give them their value
    while (count < period):
        sum = sum + what["Close"][startPoint + count]
        what["10daySMA"][startPoint+count] = what["Close"][startPoint + count]
        count = count + 1
    #first average, and now index is 5
    average = sum / period
    what["10daySMA"][startPoint + count] = average #index is five, and first SMA period 5 
    startPoint = startPoint + 1
    while (startPoint < numEntries - period):
        #need to update the sum
        sum = 0
        count = 0
        while (count < period):
            sum = sum + what["Close"][startPoint + count]
            count = count + 1
        #end of the second while loop, update the SMA5
        average = sum / period
        what["10daySMA"][startPoint + count] = average
        startPoint = startPoint + 1
#EFFECTS: Calculate fifty Day Average SMA
def fiftydayaverage(what):
    numEntries = len(what["Open"]) #end of entry number
    startPoint = 0
    average = 0 
    count = 0
    sum = 0
    period = 50
    #we know that the very frist 5 values do not matter, give them their value
    while (count < period):
        sum = sum + what["Close"][startPoint + count]
        what["50daySMA"][startPoint+count] = what["Close"][startPoint + count]
        count = count + 1
    #first average, and now index is 5
    average = sum / period
    what["50daySMA"][startPoint + count] = average #index is five, and first SMA period 5 
    startPoint = startPoint + 1
    while (startPoint < numEntries - period):
        #need to update the sum
        sum = 0
        count = 0
        while (count < period):
            sum = sum + what["Close"][startPoint + count]
            count = count + 1
        #end of the second while loop, update the SMA5
        average = sum / period
        what["50daySMA"][startPoint + count] = average
        startPoint = startPoint + 1


#EFFECTS: Calculate Hundred Day Average SMA
def hundreddayaverage(what):
    numEntries = len(what["Open"]) #end of entry number
    startPoint = 0
    average = 0 
    count = 0
    sum = 0
    period = 50
    #we know that the very frist 5 values do not matter, give them their value
    while (count < period):
        sum = sum + what["Close"][startPoint + count]
        what["100daySMA"][startPoint+count] = what["Close"][startPoint + count]
        count = count + 1
    #first average, and now index is 5
    average = sum / period
    what["100daySMA"][startPoint + count] = average #index is five, and first SMA period 5 
    startPoint = startPoint + 1
    while (startPoint < numEntries - period):
        #need to update the sum
        sum = 0
        count = 0
        while (count < period):
            sum = sum + what["Close"][startPoint + count]
            count = count + 1
        #end of the second while loop, update the SMA5
        average = sum / period
        what["100daySMA"][startPoint + count] = average
        startPoint = startPoint + 1

#EFFECTS: takes in preiod and name of col, and calculate EMA according to that period
#and save the results to according column
def EMA(what, period, col): #takes in pandas dataframd and integer representing period and string column name
    numEntries = len(what["Open"]) #end of entry number
    multiplier = (2 / (period + 1))
    index = period
    preEMA = 0
    count = 0
    sum = 0
    #We need to calculate SMA for first "previous EMA"
    while (count < period):
        sum = sum + what["Close"][count]
        what[col][count] = what["Close"][count]
        count = count + 1
    #Assigning first EMA value
    preEMA = sum / period
    what[col][index] = ((what["Close"][index] - preEMA) * multiplier) + preEMA
    preEMA = what[col][index]
    index = index + 1
    #EMA values for the rest of entries
    while (index < numEntries):
        what[col][index] = ((what["Close"][index] - preEMA) * multiplier) + preEMA
        preEMA = what[col][index] #update the preEMA
        index = index + 1 #update the index

def nine_day_MACD(what, period, col): #takes in pandas dataframd and integer representing period and string column name
    numEntries = len(what["Open"]) #end of entry number
    multiplier = (2 / (period + 1))
    index = period
    preEMA = 0
    count = 0
    sum = 0
    #We need to calculate SMA for first "previous EMA"
    while (count < period):
        sum = sum + what["MACD"][count]
        what[col][count] = what["MACD"][count]
        count = count + 1
    #Assigning first EMA value
    preEMA = sum / period
    what[col][index] = ((what["MACD"][index] - preEMA) * multiplier) + preEMA
    preEMA = what[col][index]
    index = index + 1
    #EMA values for the rest of entries
    while (index < numEntries):
        what[col][index] = ((what["MACD"][index] - preEMA) * multiplier) + preEMA
        preEMA = what[col][index] #update the preEMA
        index = index + 1 #update the index        

#MACD Calculation function
def MACD(what):
    #Create EMA 12 day and 26 day
    what["26dayEMA"] = pd.Series(np.random.randn(len(what["Open"])), index=what.index)
    what["12dayEMA"] = pd.Series(np.random.randn(len(what["Open"])), index=what.index)
    what["signal"] = pd.Series(np.random.randn(len(what["Open"])), index=what.index)
    EMA(what, 26, "26dayEMA")
    EMA(what, 12, "12dayEMA")
    
    #MACD Line: (12-day EMA - 26-day EMA)
    what["MACD"] = pd.Series(np.random.randn(len(what["Open"])), index=what.index)
    what["MACD"] = what["12dayEMA"] - what["26dayEMA"]
    nine_day_MACD(what, 9, "signal")

#RSI calc
def RSICalc(what):
    #we are going to calculate period = 14 following the recipe by J. Welles Wilder, Jr.
    #gain if diff is bigger than 0, loss if diff is less than 0
    #create an array of size 14
    numEntries = len(what["Open"])
    diff = pd.DataFrame.diff(what["Close"])
    gain = np.array([])
    loss = np.array([])
    index = 0 
    diff[index] = 0
    while (index < 14):
        if(diff[index] >= 0):
            gain = np.insert(gain,0,diff[index])
           
        elif(diff[index] < 0):
            loss = np.insert(loss,0,diff[index])
        what["RSI"][index] = 0
        index = index + 1
    #Ready to calculate RS and RSI
   
    gain_avg = np.sum(gain) / 14

    loss_avg = abs(np.sum(loss)) / 14

    RS = gain_avg / loss_avg
    RSI = 100 - (100/(1+RS))

    what["RSI"][index] = RSI
    while (index < numEntries):
        #first we need to delete the first added number to each Gain and Loss
        if(diff[index] >= 0):
            gain_avg = ((13 * gain_avg) + diff[index]) / 14
            loss_avg = ((13 * loss_avg))/14
        elif(diff[index] < 0):
            loss_avg = abs(((13 * loss_avg) + abs(diff[index])) / 14)
            gain_avg = ((13 * gain_avg)) / 14
        RS = gain_avg / loss_avg
        RSI = 100 - (100/(1+RS))
        what["RSI"][index] = RSI
        index = index + 1

#EFFECTS: PopUp Message
def popupmsg(msg):
    popup = tk.Tk()
    def leavemini():
       popup.destroy()

    popup.wm_title("!")
       
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text = "Okay", command = leavemini)
    B1.pack()

    popup.mainloop()

#EFFECTS: Display Graphs, and update 
def animate(i):
    global refreshRate
    global DatCounter
    global stock

    if stock == "S&P500":
        a = plt.subplot2grid((10,4), (1,0), rowspan=6, colspan=4)
        a2 = plt.subplot2grid((10,4), (8,0), sharex=a, rowspan=2, colspan=4)
        mydata = Quandl.get("YAHOO/INDEX_GSPC")
        high = mydata["High"]
        low = mydata["Low"]
        high = high[13000:]
        low = low[13000:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[13000:]

        a.clear()
        a.plot(high, color = 'green')
        a.plot(low, color = 'red')
        a2.plot(diff, color = 'black')
        #fix legend issue
        title = "S&P 500 Highs, and Lows data graph. Current High:" + str(high[-1]) + "Current Low:" + str(low[-1])
        a.set_title(title)
        a2.set_title("Difference between High and Low")
        a.legend(bbox_to_anchor = (0, 1.02, 1, .102), loc = 2, ncol = 1, borderaxespad=0)
   
    elif stock == "GOOGLE":
        
        a = plt.subplot2grid((16,4), (6,0), rowspan=7, colspan=4)
        a2 = plt.subplot2grid((16,4), (14,0), sharex=a, rowspan=2, colspan=4)
        a0 = plt.subplot2grid((16,4), (0,0), sharex=a, rowspan=2, colspan=4)
        a3 = plt.subplot2grid((16,4), (3,0), sharex=a, rowspan=2, colspan=4) #plotting MACD

        mydata = Quandl.get("GOOG/NASDAQ_GOOG")
        sLength = len(mydata["Open"])
        mydata["RSI"] = pd.Series(np.random.randn(sLength), index=mydata.index)
        

        high = mydata["High"]
        low = mydata["Low"]
        volume = (mydata["Volume"] * mydata["Close"]) / 1e6 #Dollar Volume in Millions
        volume = volume[2700:]
        high = high[2700:]
        low = low[2700:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[2700:]

        a.clear()
        a2.clear()
        a3.clear()
        a0.clear()
   
        #Checking SMA short periods
        if SMA_short_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2700:]
            a.plot(SMA5, color = 'blue',lw = 2)
        elif SMA_short_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2700:]
            a.plot(SMA10,color = 'blue')
        elif SMA_short_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2700:]
            a.plot(SMA50,color = 'blue')
        elif SMA_short_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2700:]
            a.plot(SMA100,color = 'blue')

        #Checking SMA long periods
        if SMA_long_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2700:]
            a.plot(SMA5, color = 'black',)
        elif SMA_long_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2700:]
            a.plot(SMA10,color = 'black')
        elif SMA_long_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2700:]
            a.plot(SMA50,color = 'black',lw = 2)
        elif SMA_long_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2700:]
            a.plot(SMA100,color = 'black')

        #Checking EMA short periods
        if EMA_short_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2700:]
            a.plot(EMA5, color = 'red')
        elif EMA_short_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2700:]
            a.plot(EMA10,color = 'red')
        elif EMA_short_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2700:]
            a.plot(EMA50,color = 'red')
        elif EMA_short_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2700:]
            a.plot(EMA100,color = 'red')
        elif EMA_short_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2700:]
            a.plot(EMA250,color = 'red')

        #Checking EMA long periods
        if EMA_long_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2700:]
            a.plot(EMA5, color = 'purple',)
        elif EMA_long_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2700:]
            a.plot(EMA10,color = 'purple')
        elif EMA_long_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2700:]
            a.plot(EMA50,color = 'purple')
        elif EMA_long_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2700:]
            a.plot(EMA100,color = 'purple')
        elif EMA_long_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2700:]
            a.plot(EMA250,color = 'purple')



        aa = a.twinx()
        max = volume.max()
        aa.set_ylim(0, 5*max)
        aa.set_yticks([])
        aa.fill_between(volume.index, volume, 0, facecolor = 'black', edgecolor='blue')

        MACD(mydata)
        a3.plot(mydata["MACD"][2700:], color = 'black')
        a3.plot(mydata["signal"][2700:], color = 'red')


        RSICalc(mydata)
        RSI = mydata["RSI"]
        RSI = RSI[2700:]
        a0.set_ylim(0, 100)
        a0.plot(RSI, color = 'brown')
        a0.axhline(70, color='black')
        a0.axhline(30, color= 'black')
        a0.text(0.6, 0.9, '>70 = overbought', va='top', transform=a0.transAxes, fontsize=9)
        a0.text(0.6, 0.1, '<30 = oversold', transform=a0.transAxes, fontsize=9)

        a2.plot(diff, color = 'black')
        a2.fill_between(diff.index, diff, 0,  facecolor='green', edgecolor='black')

        title = "Google inc. Current High: " + str(high[-1]) + " Current Low: " + str(low[-1])
        a.set_title(title)
        a0_title = "Current Relative Strength Index is: " + str(RSI[-1])
        a0.set_title(a0_title)
        a2.set_title("Difference between High and Low")
        a3.set_title("MACD")
        a.legend(loc=0)
        a0.legend(loc=0)
        a3.legend(loc=0)
       

    elif stock == "TESLA":
        a = plt.subplot2grid((16,4), (6,0), rowspan=7, colspan=4)
        a2 = plt.subplot2grid((16,4), (14,0), sharex=a, rowspan=2, colspan=4)
        a0 = plt.subplot2grid((16,4), (0,0), sharex=a, rowspan=2, colspan=4)
        a3 = plt.subplot2grid((16,4), (3,0), sharex=a, rowspan=2, colspan=4) #plotting MACD

        mydata =  Quandl.get("YAHOO/TSLA")
        sLength = len(mydata["Open"])
        mydata["RSI"] = pd.Series(np.random.randn(sLength), index=mydata.index)
        

        high = mydata["High"]
        low = mydata["Low"]
        volume = (mydata["Volume"] * mydata["Close"]) / 1e6 #Dollar Volume in Millions
        volume = volume[2500:]
        high = high[2500:]
        low = low[2500:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[2500:]

        a.clear()
        a2.clear()
        a3.clear()
        a0.clear()
   
        #Checking SMA short periods
        if SMA_short_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2500:]
            a.plot(SMA5, color = 'blue',lw = 2)
        elif SMA_short_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2500:]
            a.plot(SMA10,color = 'blue')
        elif SMA_short_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2500:]
            a.plot(SMA50,color = 'blue')
        elif SMA_short_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2500:]
            a.plot(SMA100,color = 'blue')

        #Checking SMA long periods
        if SMA_long_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2500:]
            a.plot(SMA5, color = 'black',)
        elif SMA_long_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2500:]
            a.plot(SMA10,color = 'black')
        elif SMA_long_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2500:]
            a.plot(SMA50,color = 'black',lw = 2)
        elif SMA_long_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2500:]
            a.plot(SMA100,color = 'black')

        #Checking EMA short periods
        if EMA_short_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2500:]
            a.plot(EMA5, color = 'red')
        elif EMA_short_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2500:]
            a.plot(EMA10,color = 'red')
        elif EMA_short_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2500:]
            a.plot(EMA50,color = 'red')
        elif EMA_short_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2500:]
            a.plot(EMA100,color = 'red')
        elif EMA_short_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2500:]
            a.plot(EMA250,color = 'red')

        #Checking EMA long periods
        if EMA_long_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2500:]
            a.plot(EMA5, color = 'purple',)
        elif EMA_long_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2500:]
            a.plot(EMA10,color = 'purple')
        elif EMA_long_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2500:]
            a.plot(EMA50,color = 'purple')
        elif EMA_long_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2500:]
            a.plot(EMA100,color = 'purple')
        elif EMA_long_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2500:]
            a.plot(EMA250,color = 'purple')



        aa = a.twinx()
        max = volume.max()
        aa.set_ylim(0, 5*max)
        aa.set_yticks([])
        aa.fill_between(volume.index, volume, 0, facecolor = 'black', edgecolor='blue')

        MACD(mydata)
        a3.plot(mydata["MACD"][2500:], color = 'black')
        a3.plot(mydata["signal"][2500:], color = 'red')


        RSICalc(mydata)
        RSI = mydata["RSI"]
        RSI = RSI[2500:]
        a0.set_ylim(0, 100)
        a0.plot(RSI, color = 'brown')
        a0.axhline(70, color='black')
        a0.axhline(30, color= 'black')
        a0.text(0.6, 0.9, '>70 = overbought', va='top', transform=a0.transAxes, fontsize=9)
        a0.text(0.6, 0.1, '<30 = oversold', transform=a0.transAxes, fontsize=9)

        a2.plot(diff, color = 'black')
        a2.fill_between(diff.index, diff, 0,  facecolor='green', edgecolor='black')

        title = "TESLA inc. Current High: " + str(high[-1]) + " Current Low: " + str(low[-1])
        a.set_title(title)
        a0_title = "Current Relative Strength Index is: " + str(RSI[-1])
        a0.set_title(a0_title)
        a2.set_title("Difference between High and Low")
        a3.set_title("MACD")
        a.legend(loc=0)
        a0.legend(loc=0)
        a3.legend(loc=0)

    elif stock == "YAHOO":

        a = plt.subplot2grid((16,4), (6,0), rowspan=7, colspan=4)
        a2 = plt.subplot2grid((16,4), (14,0), sharex=a, rowspan=2, colspan=4)
        a0 = plt.subplot2grid((16,4), (0,0), sharex=a, rowspan=2, colspan=4)
        a3 = plt.subplot2grid((16,4), (3,0), sharex=a, rowspan=2, colspan=4) #plotting MACD

        mydata =  Quandl.get("YAHOO/YHOO")
        sLength = len(mydata["Open"])
        mydata["RSI"] = pd.Series(np.random.randn(sLength), index=mydata.index)
        

        high = mydata["High"]
        low = mydata["Low"]
        volume = (mydata["Volume"] * mydata["Close"]) / 1e6 #Dollar Volume in Millions
        volume = volume[500:]
        high = high[500:]
        low = low[500:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[500:]

        a.clear()
        a2.clear()
        a3.clear()
        a0.clear()
   
        #Checking SMA short periods
        if SMA_short_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[500:]
            a.plot(SMA5, color = 'blue',lw = 2)
        elif SMA_short_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[500:]
            a.plot(SMA10,color = 'blue')
        elif SMA_short_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[500:]
            a.plot(SMA50,color = 'blue')
        elif SMA_short_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[500:]
            a.plot(SMA100,color = 'blue')

        #Checking SMA long periods
        if SMA_long_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[500:]
            a.plot(SMA5, color = 'black',)
        elif SMA_long_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[500:]
            a.plot(SMA10,color = 'black')
        elif SMA_long_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[500:]
            a.plot(SMA50,color = 'black',lw = 2)
        elif SMA_long_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[500:]
            a.plot(SMA100,color = 'black')

        #Checking EMA short periods
        if EMA_short_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[500:]
            a.plot(EMA5, color = 'red')
        elif EMA_short_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[500:]
            a.plot(EMA10,color = 'red')
        elif EMA_short_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[500:]
            a.plot(EMA50,color = 'red')
        elif EMA_short_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[500:]
            a.plot(EMA100,color = 'red')
        elif EMA_short_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[500:]
            a.plot(EMA250,color = 'red')

        #Checking EMA long periods
        if EMA_long_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[500:]
            a.plot(EMA5, color = 'purple',)
        elif EMA_long_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[500:]
            a.plot(EMA10,color = 'purple')
        elif EMA_long_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[500:]
            a.plot(EMA50,color = 'purple')
        elif EMA_long_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[500:]
            a.plot(EMA100,color = 'purple')
        elif EMA_long_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[500:]
            a.plot(EMA250,color = 'purple')



        aa = a.twinx()
        max = volume.max()
        aa.set_ylim(0, 5*max)
        aa.set_yticks([])
        aa.fill_between(volume.index, volume, 0, facecolor = 'black', edgecolor='blue')

        MACD(mydata)
        a3.plot(mydata["MACD"][500:], color = 'black')
        a3.plot(mydata["signal"][500:], color = 'red')


        RSICalc(mydata)
        RSI = mydata["RSI"]
        RSI = RSI[500:]
        a0.set_ylim(0, 100)
        a0.plot(RSI, color = 'brown')
        a0.axhline(70, color='black')
        a0.axhline(30, color= 'black')
        a0.text(0.6, 0.9, '>70 = overbought', va='top', transform=a0.transAxes, fontsize=9)
        a0.text(0.6, 0.1, '<30 = oversold', transform=a0.transAxes, fontsize=9)

        a2.plot(diff, color = 'black')
        a2.fill_between(diff.index, diff, 0,  facecolor='green', edgecolor='black')

        title = "Yahoo inc. Current High: " + str(high[-1]) + " Current Low: " + str(low[-1])
        a.set_title(title)
        a0_title = "Current Relative Strength Index is: " + str(RSI[-1])
        a0.set_title(a0_title)
        a2.set_title("Difference between High and Low")
        a3.set_title("MACD")
        a.legend(loc=0)
        a0.legend(loc=0)
        a3.legend(loc=0)

    elif stock == "FACEBOOK":

        a = plt.subplot2grid((16,4), (6,0), rowspan=7, colspan=4)
        a2 = plt.subplot2grid((16,4), (14,0), sharex=a, rowspan=2, colspan=4)
        a0 = plt.subplot2grid((16,4), (0,0), sharex=a, rowspan=2, colspan=4)
        a3 = plt.subplot2grid((16,4), (3,0), sharex=a, rowspan=2, colspan=4) #plotting MACD

        mydata =  Quandl.get("GOOG/NASDAQ_FB")
        sLength = len(mydata["Open"])
        mydata["RSI"] = pd.Series(np.random.randn(sLength), index=mydata.index)
        

        high = mydata["High"]
        low = mydata["Low"]
        volume = (mydata["Volume"] * mydata["Close"]) / 1e6 #Dollar Volume in Millions
        volume = volume[500:]
        high = high[500:]
        low = low[500:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[500:]

        a.clear()
        a2.clear()
        a3.clear()
        a0.clear()
   
        #Checking SMA short periods
        if SMA_short_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[500:]
            a.plot(SMA5, color = 'blue',lw = 2)
        elif SMA_short_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[500:]
            a.plot(SMA10,color = 'blue')
        elif SMA_short_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[500:]
            a.plot(SMA50,color = 'blue')
        elif SMA_short_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[500:]
            a.plot(SMA100,color = 'blue')

        #Checking SMA long periods
        if SMA_long_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[500:]
            a.plot(SMA5, color = 'black',)
        elif SMA_long_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[500:]
            a.plot(SMA10,color = 'black')
        elif SMA_long_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[500:]
            a.plot(SMA50,color = 'black',lw = 2)
        elif SMA_long_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[500:]
            a.plot(SMA100,color = 'black')

        #Checking EMA short periods
        if EMA_short_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[500:]
            a.plot(EMA5, color = 'red')
        elif EMA_short_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[500:]
            a.plot(EMA10,color = 'red')
        elif EMA_short_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[500:]
            a.plot(EMA50,color = 'red')
        elif EMA_short_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[500:]
            a.plot(EMA100,color = 'red')
        elif EMA_short_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[500:]
            a.plot(EMA250,color = 'red')

        #Checking EMA long periods
        if EMA_long_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[500:]
            a.plot(EMA5, color = 'purple',)
        elif EMA_long_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[500:]
            a.plot(EMA10,color = 'purple')
        elif EMA_long_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[500:]
            a.plot(EMA50,color = 'purple')
        elif EMA_long_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[500:]
            a.plot(EMA100,color = 'purple')
        elif EMA_long_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[500:]
            a.plot(EMA250,color = 'purple')



        aa = a.twinx()
        max = volume.max()
        aa.set_ylim(0, 5*max)
        aa.set_yticks([])
        aa.fill_between(volume.index, volume, 0, facecolor = 'black', edgecolor='blue')

        MACD(mydata)
        a3.plot(mydata["MACD"][500:], color = 'black')
        a3.plot(mydata["signal"][500:], color = 'red')


        RSICalc(mydata)
        RSI = mydata["RSI"]
        RSI = RSI[500:]
        a0.set_ylim(0, 100)
        a0.plot(RSI, color = 'brown')
        a0.axhline(70, color='black')
        a0.axhline(30, color= 'black')
        a0.text(0.6, 0.9, '>70 = overbought', va='top', transform=a0.transAxes, fontsize=9)
        a0.text(0.6, 0.1, '<30 = oversold', transform=a0.transAxes, fontsize=9)

        a2.plot(diff, color = 'black')
        a2.fill_between(diff.index, diff, 0,  facecolor='green', edgecolor='black')

        title = "Facebook inc. Current High: " + str(high[-1]) + " Current Low: " + str(low[-1])
        a.set_title(title)
        a0_title = "Current Relative Strength Index is: " + str(RSI[-1])
        a0.set_title(a0_title)
        a2.set_title("Difference between High and Low")
        a3.set_title("MACD")
        a.legend(loc=0)
        a0.legend(loc=0)
        a3.legend(loc=0)


    elif stock == "APPLE":

        a = plt.subplot2grid((16,4), (6,0), rowspan=7, colspan=4)
        a2 = plt.subplot2grid((16,4), (14,0), sharex=a, rowspan=2, colspan=4)
        a0 = plt.subplot2grid((16,4), (0,0), sharex=a, rowspan=2, colspan=4)
        a3 = plt.subplot2grid((16,4), (3,0), sharex=a, rowspan=2, colspan=4) #plotting MACD

        mydata =  Quandl.get("GOOG/NASDAQ_AAPL")
        sLength = len(mydata["Open"])
        mydata["RSI"] = pd.Series(np.random.randn(sLength), index=mydata.index)
        

        high = mydata["High"]
        low = mydata["Low"]
        volume = (mydata["Volume"] * mydata["Close"]) / 1e6 #Dollar Volume in Millions
        volume = volume[2500:]
        high = high[2500:]
        low = low[2500:]
        diff = mydata["High"] - mydata["Low"]
        diff = diff[2500:]

        a.clear()
        a2.clear()
        a3.clear()
        a0.clear()
   
        #Checking SMA short periods
        if SMA_short_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2500:]
            a.plot(SMA5, color = 'blue',lw = 2)
        elif SMA_short_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2500:]
            a.plot(SMA10,color = 'blue')
        elif SMA_short_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2500:]
            a.plot(SMA50,color = 'blue')
        elif SMA_short_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2500:]
            a.plot(SMA100,color = 'blue')

        #Checking SMA long periods
        if SMA_long_periods == 5:
            mydata["5daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            fivedayaverage(mydata)
            SMA5 = mydata["5daySMA"]
            SMA5 = SMA5[2500:]
            a.plot(SMA5, color = 'black',)
        elif SMA_long_periods == 10:
            mydata["10daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            tendayaverage(mydata)
            SMA10 = mydata["10daySMA"]
            SMA10 = SMA10[2500:]
            a.plot(SMA10,color = 'black')
        elif SMA_long_periods == 50:
            mydata["50daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            fiftydayaverage(mydata)
            SMA50 = mydata["50daySMA"]
            SMA50 = SMA50[2500:]
            a.plot(SMA50,color = 'black',lw = 2)
        elif SMA_long_periods == 100:
            mydata["100daySMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            hundreddayaverage(mydata)
            SMA100 = mydata["100daySMA"]
            SMA100 = SMA100[2500:]
            a.plot(SMA100,color = 'black')

        #Checking EMA short periods
        if EMA_short_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2500:]
            a.plot(EMA5, color = 'red')
        elif EMA_short_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2500:]
            a.plot(EMA10,color = 'red')
        elif EMA_short_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2500:]
            a.plot(EMA50,color = 'red')
        elif EMA_short_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2500:]
            a.plot(EMA100,color = 'red')
        elif EMA_short_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2500:]
            a.plot(EMA250,color = 'red')

        #Checking EMA long periods
        if EMA_long_periods == 5:
            mydata["5dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index) #5 day index
            EMA(mydata, 5, "5dayEMA")
            EMA5 = mydata["5dayEMA"]
            EMA5 = EMA5[2500:]
            a.plot(EMA5, color = 'purple',)
        elif EMA_long_periods == 10:
            mydata["10dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 10, "10dayEMA")
            EMA10 = mydata["10dayEMA"]
            EMA10 = EMA10[2500:]
            a.plot(EMA10,color = 'purple')
        elif EMA_long_periods == 50:
            mydata["50dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata,50,"50dayEMA")
            EMA50 = mydata["50dayEMA"]
            EMA50 = EMA50[2500:]
            a.plot(EMA50,color = 'purple')
        elif EMA_long_periods == 100:
            mydata["100dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 100, "100dayEMA")
            EMA100 = mydata["100dayEMA"]
            EMA100 = EMA100[2500:]
            a.plot(EMA100,color = 'purple')
        elif EMA_long_periods == 250:
            mydata["250dayEMA"] = pd.Series(np.random.randn(sLength), index=mydata.index)
            EMA(mydata, 250, "250dayEMA")
            EMA250 = mydata["250dayEMA"]
            EMA250 = EMA250[2500:]
            a.plot(EMA250,color = 'purple')



        aa = a.twinx()
        max = volume.max()
        aa.set_ylim(0, 5*max)
        aa.set_yticks([])
        aa.fill_between(volume.index, volume, 0, facecolor = 'black', edgecolor='blue')

        MACD(mydata)
        a3.plot(mydata["MACD"][2500:], color = 'black')
        a3.plot(mydata["signal"][2500:], color = 'red')


        RSICalc(mydata)
        RSI = mydata["RSI"]
        RSI = RSI[2500:]
        a0.set_ylim(0, 100)
        a0.plot(RSI, color = 'brown')
        a0.axhline(70, color='black')
        a0.axhline(30, color= 'black')
        a0.text(0.6, 0.9, '>70 = overbought', va='top', transform=a0.transAxes, fontsize=9)
        a0.text(0.6, 0.1, '<30 = oversold', transform=a0.transAxes, fontsize=9)

        a2.plot(diff, color = 'black')
        a2.fill_between(diff.index, diff, 0,  facecolor='green', edgecolor='black')

        title = "Apple inc. Current High: " + str(high[-1]) + " Current Low: " + str(low[-1])
        a.set_title(title)
        a0_title = "Current Relative Strength Index is: " + str(RSI[-1])
        a0.set_title(a0_title)
        a2.set_title("Difference between High and Low")
        a3.set_title("MACD")
        a.legend(loc=0)
        a0.legend(loc=0)
        a3.legend(loc=0)

        
class MenuBarProgram(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SMA/EMA/RSI/MACD graphing tool")
        global stock
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="S&P 500", command=lambda: changeStock("S&P500"))
        filemenu.add_command(label="GOOGLE", command=lambda: changeStock("GOOGLE"))
        filemenu.add_command(label="FACEBOOK", command=lambda: changeStock("FACEBOOK"))
        filemenu.add_command(label="APPLE", command=lambda: changeStock("APPLE"))
        filemenu.add_command(label="YAHOO", command=lambda: changeStock("YAHOO"))
        filemenu.add_command(label="TESLA", command=lambda: changeStock("TESLA"))
        menubar.add_cascade(label="STOCKS", menu=filemenu)


        dataShortSMA = tk.Menu(menubar, tearoff=1)
        dataShortSMA.add_command ( label="5 Days",
                                  command=lambda: change_Short_SMA(5) )
        dataShortSMA.add_command ( label="10 Days",
                                  command=lambda: change_Short_SMA(10))
        dataShortSMA.add_command ( label="50 Days",
                                  command=lambda: change_Short_SMA(50) )
        dataShortSMA.add_command ( label="100 Days",
                                  command=lambda: change_Short_SMA(100) )
        menubar.add_cascade(label = "SMA Short-Term Periods", menu = dataShortSMA)



        dataLongSMA = tk.Menu(menubar, tearoff=1)
        dataLongSMA.add_command ( label="5 Days",
                                  command=lambda: change_Long_SMA(5) )
        dataLongSMA.add_command ( label="10 Days",
                                  command=lambda: change_Long_SMA(10))
        dataLongSMA.add_command ( label="50 Days",
                                  command=lambda: change_Long_SMA(50) )
        dataLongSMA.add_command ( label="100 Days",
                                  command=lambda: change_Long_SMA(100) )
        menubar.add_cascade(label = "SMA Long-Term Periods", menu = dataLongSMA)

        dataShortEMA = tk.Menu(menubar, tearoff=1)
        dataShortEMA.add_command ( label="5 Days",
                                  command=lambda: change_Short_EMA(5) )
        dataShortEMA.add_command ( label="10 Days",
                                  command=lambda: change_Short_EMA(10))
        dataShortEMA.add_command ( label="50 Days",
                                  command=lambda: change_Short_EMA(50) )
        dataShortEMA.add_command ( label="100 Days",
                                  command=lambda: change_Short_EMA(100) )
        dataShortEMA.add_command ( label="250 Days",
                                  command=lambda: change_Short_EMA(250) )
        menubar.add_cascade(label = "EMA Short-Term Periods", menu = dataShortEMA)

        dataLongEMA = tk.Menu(menubar, tearoff=1)
        dataLongEMA.add_command ( label="5 Days",
                                  command=lambda: change_Long_EMA(5) )
        dataLongEMA.add_command ( label="10 Days",
                                  command=lambda: change_Long_EMA(10))
        dataLongEMA.add_command ( label="50 Days",
                                  command=lambda: change_Long_EMA(50) )
        dataLongEMA.add_command ( label="100 Days",
                                  command=lambda: change_Long_EMA(100) )
        dataLongEMA.add_command ( label="250 Days",
                                  command=lambda: change_Long_EMA(250) )
        menubar.add_cascade(label = "EMA Long-Term Periods", menu = dataLongEMA)



        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="What is SMA?", command=tutorial)
        helpmenu.add_command(label="What is EMA?", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)
        

        self.frames = {}
        for F in (StartPage, HomePage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

      

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="""This SMA and EMA graphing tool is desinged to give 
            traders guidance on when to buy or sell. Historically, both SMA and EMA have been 
            widely used by traders. Use it with your own discretion. If you wish not to use this 
            tool, press disagree, otherwise press agree""", font=LARGE_FONT)


        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Agree", 
                            command=lambda: controller.show_frame(HomePage))
        button2 = ttk.Button(self, text="Disagree",
                            command=quit)
        button1.pack()
        button2.pack()

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="SMA/EMA/RSI/MACD graphing tool", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg( canvas, self )
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)



app = MenuBarProgram()
app.geometry("1280x720")
ani = animation.FuncAnimation(f,animate, interval=8000)
app.mainloop()
