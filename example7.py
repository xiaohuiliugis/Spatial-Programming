import arcpy

rows = arcpy.da.SearchCursor(r"C:\Xiaohui\Spatial Programming\w7\data\Parks.shp", ["Name", "SHAPE@"])

rownumber =0
for row in rows:
    print row,row[0],row[1]
    for partnumber in range(0,row[1].partCount):
        print "Row: " + str(rownumber)
        print "Part:" + str(partnumber)

        part = row[1].getPart(partnumber)
        for pt in part:
            print pt
    rownumber +=1

##    for pt in part:
##        print pt.X


