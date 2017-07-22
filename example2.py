import arcpy

arcpy.env.overwriteOutput = True

fc = r"C:\Xiaohui\Spatial Programming\w8\Cityi10.shp"
fc2 = r"C:\Xiaohui\Spatial Programming\w8\Cityi10_copy2.shp"

arcpy.Copy_management(fc, fc2)

fields = ["Name10", "SHAPE@"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        print row[0]
        partnum = 0
        # Step through each part of the feature
        #
        points = []
        for part in row[1]:
            # Print the part number
            #
            print row[1]
            print("Part {0}:".format(partnum))

            # Step through each vertex in the feature
            #
            for pnt in part:
                if pnt:
                    # Print x,y coordinates of current point
                    #
                    points.append((pnt.X, pnt.Y))
                    #print("{0}, {1}".format(pnt.X, pnt.Y))
                else:
                    # If pnt is None, this represents an interior ring
                    #
                    pass
                    #print("Interior Ring:")
            partnum += 1
        print partnum

del cursor, row
