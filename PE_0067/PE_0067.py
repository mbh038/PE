# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 04:25:27 2016

@author: Mike
"""
import time
def PE_0067(filename):
    start_time = time.time()
    triangle = readcsv(filename)
#    print triangle
    frontier=triangle[-1]
    for line in range(len(triangle)-2,-1,-1):
        newFrontier=[]
        for number in range(len(triangle[line])):
            newFrontier.append(triangle[line][number]+max(frontier[number],frontier[number+1]))           
        frontier=newFrontier
    print ' Maximum sum=: ',frontier[0]  
    print("--- %s seconds ---" % (time.time() - start_time))      
    return frontier
    
def readcsv (filename):
    #Import the string functions from python
    import string
    
    # 1) Splits the text file into individual characters
    # to identify the commas and parsing the individual 
    # tokens.
    
    # create a list to store the inputted numbers
    numbers = list()
    # Open the input text file for reading
    dataFile = open(filename, 'r')
    
    # Loop through each line of the input data file
    for eachLine in dataFile:
        numbersline=list()
    # setup a temporay variable
        tmpStr = ''
        # loop through each character in the line
        for char in eachLine:
            # check whether the char is a number
            if char.isdigit():
                # if it is a number add it to the tmpStr
                tmpStr += char
                # if a comma is identified and tmpStr has a 
                # value then append it to the numbers list
            elif char == ',' and tmpStr != '':
                numbersline.append(int(tmpStr))
                tmpStr = ''
        # if the tmpStr contains a number add it to the 
        # numbers list.
        if tmpStr.isdigit():
            numbersline.append(int(tmpStr))
        numbers.append(numbersline)
    # Print the number list
    #print numbers
    # Close the input data file.
    dataFile.close()
    return numbers