
import arcpy
arcpy.env.overwriteOutput =True
fc = r"C:\Xiaohui\Spatial Programming\w8\Cityi10.shp"
fc2 = r"C:\Xiaohui\Spatial Programming\w8\Copy_Cityi10.shp"

fields = ["Name10","SHAPE@"]

arcpy.CreateFeatureclass_management(r"C:\Xiaohui\Spatial Programming\w8", "diff.shp", "POLYGON")

arcpy.Copy_management(fc, fc2)

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        #print row[0],row[1]
        polygonbuf = row[1].buffer(100)
        row[1] = polygonbuf.difference(row[1])

        print fc3
        cursor.updateRow(row) 
