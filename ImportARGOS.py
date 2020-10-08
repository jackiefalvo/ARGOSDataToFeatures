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
