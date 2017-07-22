
import arcpy

rows = arcpy.da.SearchCursor(r"C:\Xiaohui\Spatial Programming\w7\w7data\data\GPS_points.shp", ["animal","SHAPE@XY"], "Animal = 3")

total =0
count =0
for row in rows:
    print row[1].centroid.x


