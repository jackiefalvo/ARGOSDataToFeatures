##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2020
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------
#%% Set up 

# import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = "V:\\Part4_ArcPy\\ARGOSTracking\\data\\ARGOSdata\\1997dg.txt"
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#%% while loop

# open file
argos1997 = open(inputFile, 'r')

# read in one line of data
line1997 = argos1997.readline()

# start while loop, while line has a true value
while line1997:
    
    # run these conditions only if the line has "Date :"
    if ("Date :" in line1997): # why the ()?
        
        # split the line (by default..? tab?)
        splitline = line1997.split()
        
        # grab info (tag ID)
        tagID = splitline[0] # how was I to know what the third thing would be? had to make a for loop to inspect..
        
        # need to read next line to get lat/lon
        line1997_next = argos1997.readline()
        
        # split this line
        splitline_next = line1997_next.split()
        
        # grab lat/long
        lat = splitline_next[2]
        lon = splitline_next[5]
        
        # print test
        print(f"tag ID = {tagID} located at {lat, lon}")
      
    # update line1997 to progreess while loop    
    line1997 = argos1997.readline()
    
# close out file
argos1997.close()

    
