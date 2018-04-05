# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 20:52:37 2018

@author: alexa
"""
#Importing pandas as pd
import pandas as pd
import numpy as np
import sys



def searchfoodcodes(targ_codes):
    

    #Import the excel file in for manipulation
    foodcodefile = pd.ExcelFile("foodcodes.xls")

    #Parse the first sheet, where the data is
    foodcodes = foodcodefile.parse(0)

    #Keep a separate copy to retrieve data
    data = foodcodefile.parse(0)

    #Take in the axis labeled "Food code" for the food numbers
    foodcodes = foodcodes['Food code']

    #Transfer to matrix for easier manipulation
    foodcodes = foodcodes.as_matrix()

    #Take in the food description into a 1D pandas series
    zarray = data["Main food description"]

    #Setting length for loop.
    num = len(foodcodes)

    #Determine where the indexes are that contain the food numbers
    locations = np.isin(foodcodes,targ_codes)

    #Set up arrays to place in foodcodes and descriptions
    keepnums = []
    keepdesc = []

    #Place each food code and descriptions into array to
    for i in range(len(locations)):
        if locations[i] == True:
            keepnums.append(foodcodes[i])
            keepdesc.append(zarray[i])

    if(np.size(keepnums) == 0):
        print("WARNING, FOOD CODE WAS NOT FOUND, WILL RECEIVE BLANK VARIABLE")


    return keepnums, keepdesc

def searchfooddesc(targ_desc):


    #Import the excel file in for manipulation
    foodcodefile = pd.ExcelFile("foodcodes.xls")

    #Parse the first sheet, where the data is
    foodcodes = foodcodefile.parse(0)

    #Keep a separate copy to retrieve data
    data = foodcodefile.parse(0)

    #Take in the axis labeled "Food code" for the food numbers
    foodcodes = foodcodes['Food code']

    #Transfer to matrix for easier manipulation
    foodcodes = foodcodes.as_matrix()

    #Take in the food description into a 1D pandas series
    zarray = data["Main food description"]

    

    #Determine where the indexes are that contain the food description
    locations = zarray.str.match(targ_desc)

    

    keepnums = []
    keepdesc = []

    for i in range(len(locations)):
        if locations[i] == True:
            keepnums.append(foodcodes[i])
            keepdesc.append(zarray[i])

    if(np.size(keepnums) == 0):
        print("WARNING, FOOD DESCRIPTION WAS NOT FOUND, WILL RECEIVE BLANK VARIABLE")


    return keepnums, keepdesc
