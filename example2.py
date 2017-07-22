import arcpy
import numpy

from arcpy.sa import *


arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r"C:\Xiaohui\Spatial Programming\w10\week10data\data\worldwidedata.gdb"
outras = Plus("prec_1","prec_2")

arr = arcpy.RasterToNumPyArray(Raster("prec_1"),nodata_to_value=0)
arr2 = arcpy.RasterToNumPyArray(Raster("prec_2"),nodata_to_value=0)
#arr.size gives the number of values in the array

outarr = numpy.maximum(arr, arr2)

myraster = arcpy.NumpyArraytToRaster(outarr)
print arr, len(arr),arr.size,arr.shape




