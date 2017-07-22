import arcpy
from arcpy.sa import *
import numpy



arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput= True
arcpy.env.workspace = r"C:\Xiaohui\Spatial Programming\w10\week10data\data\worldwidedata.gdb"

# List all the feature datasets in the
#   workspace that start with the letter prec.
datasets = arcpy.ListDatasets("prec*")

# Calculate the mean of all the precip rasters
outCellStatistics = CellStatistics(datasets,"MEAN")

outCellStatistics.save("mean_cs_prec")

