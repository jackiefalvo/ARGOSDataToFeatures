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

# import modules
import sys, os, arcpy

# allow arcpy to overwritee outputs
arcpy.env.overwriteOutput = True

# Set input variables (Hard-wired)
inputFile = "V:\\Part4_ArcPy\\ARGOSTracking\\data\\ARGOSdata\\1997dg.txt"
outputFC = "V:\Part4_ArcPy\ARGOSTracking\scratch\ARGOStrack.shp"
outputSR = arcpy.SpatialReference(54002) # creates spatial ref obj that refers to 'World Equidistant Cylindrical' 

# create empty (point) feature class, we will add features
outPath, outName = os.path.split(outputFC)
arcpy.management.CreateFeatureclass(outPath, outName, "POINT", '', '', '', outputSR)
# notice the ind shapefile files in scratch folder now include a .prj file (projection file)

# Add TagID, LC, IQ, and Date fields to the output feature class
arcpy.AddField_management(outputFC,"TagID","LONG")
arcpy.AddField_management(outputFC,"LC","TEXT")
arcpy.AddField_management(outputFC,"Date","DATE")

#%% while loop

# open file
argos1997 = open(inputFile, 'r')

# read in one line of data
line1997 = argos1997.readline()

# start while loop, while line has a true value
while line1997:
    
    # run these conditions only if the line has "Date :"
    if ("Date :" in line1997): # why the ()?
        
        # split the line (it picks up on the split delimeter? is there a default?)
        splitline = line1997.split()
        #break -- allows us to examine the splitline list
            # why does this spit out as a list? split function does this?
        
        # grab info (tag ID)
        tagID = splitline[0] # how was I to know what the third thing would be? had to make a for loop to inspect..
        date = splitline[3]
        time = splitline[4]
        LC = splitline[7]
        
        # need to read next line to get lat/lon
        line1997_next = argos1997.readline()
        
        # split this line
        splitline_next = line1997_next.split()
        #break
        
        # grab lat/long
        lat = splitline_next[2]
        lon = splitline_next[5]
        
        # print test
        print(f"tag ID = {tagID} located at {lat, lon} \n on {date} at {time} \n Location Class = {LC}")
      
    # update line1997 to progreess while loop    
    line1997 = argos1997.readline()
    
# close out file
argos1997.close()

    
