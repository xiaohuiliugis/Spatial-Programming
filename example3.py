
import arcpy

rows = arcpy.da.SearchCursor(r"C:\Xiaohui\Spatial Programming\w7\w7data\data\GPS_points.shp", ["animal","SHAPE@XY"])

total =0
count =0
for row in rows:
    print row[0],type(row[1])
    total+=row[0]
    
    count +=1

print total, count, total/count


