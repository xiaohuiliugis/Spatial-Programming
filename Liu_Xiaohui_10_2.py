import arcpy
import numpy
import datetime

from arcpy.sa import *

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r"C:\Xiaohui\Spatial Programming\w10\week10data"

#RuntimeError: Object: Error in accessing environment <extent>
dataset = r"C:\Xiaohui\Spatial Programming\w10\week10data\tydixton_watershed.shp"
desc = arcpy.Describe(dataset)
extent = desc.extent

arcpy.env.extent = extent


datasets = arcpy.ListFeatureClasses("risk*")

c = 0
for dataset in datasets:
    print dataset
    c = c+1
    ed =EucDistance(dataset,1000)
    ed.save("eucdis_"+ str(dataset).strip('"C:\Xiaohui\Spatial Programming\w10\week10data\"').rstrip('.shp')+".img")
    #ed.save(dataset.replace(".shp", ".img"))
        

    print ed
    # constant value 1000 minus raster!!!
    rev_ed = 1000.0 - ed
    #save the reversed output
    rev_ed.save("rev_" + str(dataset).strip('"C:\Xiaohui\Spatial Programming\w10\week10data\"').rstrip('.shp')+".tif")
    print rev_ed
    
    Con(IsNull(rev_ed),0,rev_ed)
    #after con operation, save the output
    rev_ed.save("f_" + str(dataset).strip('"C:\Xiaohui\Spatial Programming\w10\week10data\"').rstrip('.shp')+".tif")
    out1 = rev_ed
    out2 = out1 + rev_ed
    out3 = out2 + rev_ed


sumout = CellStatistics(out3,"SUM")
sumout.save("sumout")

#rev_ed = EucDistance(rev_ed,1000)

##programmatically find the maximun extent, and set it as the extent
## use the extent of watershed as the extent 

