import arcpy, math,SEC

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Xiaohui\Spatial Programming\w8"

def findSQPerm(area):
    x = math.sqrt(area)
    perm = x * 4
    return perm
def findCirPerm(area):
    x = math.sqrt(area)
    perm = 2 * math.pi * x
    return perm
    

fc = r"C:\Xiaohui\Spatial Programming\w8\Cityi10.shp"
fc2 = r"C:\Xiaohui\Spatial Programming\w8\Cityi10_copy.shp"
fc3 = r"C:\Xiaohui\Spatial Programming\w8\Cityi10_copy2.shp"


arcpy.CreateFeatureclass_management(r"C:\Xiaohui\Spatial Programming\w8", "Cirles.shp", "POLYGON")

arcpy.Copy_management(fc, fc2)
arcpy.Copy_management(fc, fc3)

arcpy.AddField_management(fc2, "PARA", "DOUBLE")
arcpy.AddField_management(fc2, "SHAPE2", "DOUBLE")
arcpy.AddField_management(fc2, "CIRCLE", "DOUBLE")
arcpy.AddField_management(fc2, "SCIRCLE", "DOUBLE")

#"SHAPE@" will be modified through the process, the rest 4 newly added fields will be updated with the calculated landscape metrics
fields = ["Name10", "SHAPE@","PARA","SHAPE2","CIRCLE","SCIRCLE"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:

        # 1st Index: calculate PARA
        PARA = row[1].length/row[1].area
        row[2] = PARA
        cursor.updateRow(row)

       # 2nd Index: calculate Shape index
        pa = row[1].length / row[1].area
        pa2 = findSQPerm(row[1].area) / row[1].area
        SHAPEINDEX = pa / pa2
        #populate row[4]("SHAPE2") with shape index, then update the cursor
        row[3]= SHAPEINDEX
        cursor.updateRow(row)

        # 4th Index: SCIRCLE
        SCIRCLE = row[1].length/findCirPerm(row[1].area)
        row[5]= SCIRCLE
        cursor.updateRow(row)

        # 3rd Index: CIRLE. Step through each part of the feature
        points = []

        # one theory saying that buffer the geometry with a tiny distance will help to redraw the same geometry,does not change orginal geometry
        geo = row[1].buffer(0.01)
        
        for part in geo:
            # Print the part number
            partnum = 0
            for pnt in part:
                if pnt:
                    points.append((pnt.X, pnt.Y))
                    #print("{0}, {1}".format(pnt.X, pnt.Y))
                else:
                    # If pnt is None, this represents an interior ring
                    pass
                    #print("Interior Ring:")
            partnum += 1
        try:
            ## call  make_circle function defined in SEC moudle
            circledef = SEC.make_circle(points)
            
            ## circledef[0], circledef[1] are x, y coordinates of the centroid of the circle,circledef[2] is the radius of the circle
            ##print circledef[0],circledef[1],circledef[2]

            ## First create Point object with x, y coordinates of the centroid,then create a new PointGeometry by populating the Point object
            cp = arcpy.PointGeometry(arcpy.Point(circledef[0], circledef[1]))
            
            ## buffer the centroid using the radius will create a minimum bounding (or circumscribing)circle!!
            scc = cp.buffer(circledef[2])

            ## assign the circumscribing circle to row[1]
            row[1] = scc
            cursor.updateRow(row)

            CIRCLE = geo.area/scc.area
            #print row[0],CIRCLE

            row[4]= CIRCLE
            cursor.updateRow(row)
        except:
            print row[0] + " Did not work"
        
            #arcpy.Intersect_analysis(["homerange.shp","Parks.shp"],"intersect_p_h", "ALL","","")
    cir = cp.buffer(math.sqrt(row[1].area))
    cirsm = arcpy.da.InsertCursor(r"C:\Xiaohui\Spatial Programming\w8\Circles.shp",["SHAPE@"])
    cirsm.insertRow(cir)

    # output the difference between the smallest circumscribing circle and the input polygon
    arcpy.SymDiff_analysis(fc2, fc3, "Difference.shp")
    
##    print fc_dif
##    fc_dif = scc.difference(fc2)
##    dif = arcpy.da.InsertCursor(r"C:\Xiaohui\Spatial Programming\w8\Difference.shp",["SHAPE@"])
##    dif.insertRow(fc_dif)
      

del cursor, row
