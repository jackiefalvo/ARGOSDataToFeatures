##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2020
## Author: cristiana.falvo@duke.edu (adopted from John Fay's ENV859 course)
##---------------------------------------------------------------------
#%% set up -- import modules, sets envs, set inputs/outputs, create empty fc
# import modules
import sys, os, arcpy

# allow arcpy to overwrite outputs
arcpy.env.overwriteOutput = True

# Input data and output FC
inputFile = "V:\\Part4_ArcPy\\ARGOSTracking\\data\\ARGOSdata\\1997dg.txt"
outputFC = "V:\Part4_ArcPy\ARGOSTracking\scratch\ARGOStrack.shp"

# create empty (point) feature class, we will add features
outPath, outName = os.path.split(outputFC)
outputSR = arcpy.SpatialReference(54002) # 'World Equidistant Cylindrical' 
arcpy.management.CreateFeatureclass(outPath, outName, "POINT", '', '', '', outputSR)
# notice the ind shapefile files in scratch folder now include a .prj file (projection file)

# Add TagID, LC, and Date fields to the output feature class
arcpy.AddField_management(outputFC,"TagID","LONG")
arcpy.AddField_management(outputFC,"LC","TEXT")
arcpy.AddField_management(outputFC,"Date","DATE")

# Create insert cursor (allows me to write to my blank fc)
cursor_insert = arcpy.da.InsertCursor(outputFC, ['Shape@', 'TagID', 'LC', 'Date']) 

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
        tagID = splitline[0] 
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
        
        #print(tagID, obs_lat, obs_lon)
        #break
        
        # convert lat/lon from string to float
        # translate cardinal directions to quadrants
        try:
            
            if lat[-1] == 'N':
                obs_lat = float(lat[:-1])
            else:
                obs_lat = float(lat[:-1] * -1)
            if lon[-1] == 'W':
                obs_lon = float(lon[:-1] * -1)
            else:
                obs_lon = float(lon[:-1])
                
            print(tagID, obs_lat, obs_lon)
                
            # create point object
            obsPoint = arcpy.Point()
            obsPoint.X = obs_lon
            obsPoint.Y = obs_lat
            
            # convert point to pointGeom
            inputSR = arcpy.SpatialReference(4326) # specify SR of argos pts (global lat/lon = WGS84)
            obsPointGeom = arcpy.PointGeometry(obsPoint, inputSR) 
            
            # use insert cursor to add data to fc
            feature = cursor_insert.insertRow((obsPointGeom,tagID,LC,date.replace('.','/') + ' ' + time))
            # the (()) was to squash a whole line into one argument
            
        except Exception as e: # grabs all error lines (records with lat = '???')
            print(f"Added error record {tagID} to error bucket")
        
        
    # update line1997 to progress while loop    
    line1997 = argos1997.readline()
    
# close out file
argos1997.close()

# delete insert cursor
del cursor_insert

    
