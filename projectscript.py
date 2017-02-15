# ---------------------------------------------------------------------------
# Name: Find .csv files and convert them layer files
# Purpose: To show on a map
# Author: Keyur Kulkarni
# ---------------------------------------------------------------------------

# import system modules
import arcpy
import os
from arcpy import env

# Set environment settings
env.workspace = r"K:\School\UTDallas Lab\GISC 6317\Project"
arcpy.env.overwriteOutput = True

# Make a list to store csv files
list = []

if arcpy.Exists(r"K:\School\UTDallas Lab\GISC 6317\Project"):
    for file in arcpy.ListFiles("*.csv"):
        list.append(file)

# Loop through the list to make individual csv files
for x in list:
    in_Table = x
    x_coords = "Long"
    y_coords = "Lat"
    # Split name
    filename, file_extension = os.path.splitext(x)
    saved_layer = filename + ".lyr"

    # Make the XY event layer
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords,
                                            filename)

    # Print the total rows
    count = arcpy.GetCount_management(filename)
    print count

    # Save to a layer file
    arcpy.SaveToLayerFile_management(filename, saved_layer)

"""
    # Save layer file to a shapefile for added functionality
    arcpy.CopyFeatures_management(saved_Layer, "candidates.shp")

"""

print "Layer files saved"

# Layer to store layer files in directory
listlayers = []

if arcpy.Exists(r"K:\School\UTDallas Lab\GISC 6317\Project"):

    for file in arcpy.ListFiles("*.lyr"):
        listlayers.append(file)
print listlayers

# Loop through the list to add each layer to the map and save the map
map = r"K:\School\UTDallas Lab\GISC 6317\Project\twit.mxd"
for x in listlayers:
    mxd = arcpy.mapping.MapDocument(map)
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    addLayer = arcpy.mapping.Layer(x)
    arcpy.mapping.AddLayer(df, addLayer, "TOP")
    mxd.save()
    del mxd, addLayer
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

print "Layer files displayed on the map"

