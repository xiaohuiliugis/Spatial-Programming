# This will run only in 32 bit IDLE

import fiona
import shapely
import math, SEC
from shapely.geometry import shape, mapping
from shapely.geometry import Point,Polygon
import ogr
driver = ogr.GetDriverByName('ESRI Shapefile')

inputdataset = r"C:\Xiaohui\Spatial Programming\w9\Cityi10.shp"
outputDataset = r"C:\Xiaohui\Spatial Programming\w9\Cityi10_OpenSource.shp"
diff = r"C:\Xiaohui\Spatial Programming\w9\Difference.shp"
sameA = r"C:\Xiaohui\Spatial Programming\w9\SameArea.shp"

def findCirPerm(area):
    x = math.sqrt(area)
    perm = 2 * math.pi * x
    return perm

c = fiona.open(inputdataset, 'r')

outdiver = c.driver
outschema = c.schema.copy()
outcrs = c.crs.copy()

#outschema['geometry'] = 'Polygon'

outschema['properties']['PARA'] = 'float'
outschema['properties']['ShapeIndex'] = 'float'
outschema['properties']['CIRCLE'] = 'float'
outschema['properties']['SCIRCLE'] = 'float'
print outschema

with fiona.open(outputDataset, 'w', driver=outdiver, crs=outcrs, schema=outschema) as w:

   for rec in c:
      geom = shape(rec["geometry"])
      prim = geom.length
      area = geom.area
      p_a = (prim/area)
      SI = p_a / ((math.sqrt(area) * 4)/area)
      SCIR = geom.length/findCirPerm(geom.area)

      geonew = geom.buffer(0.01)
      
      #TypeError: 'Polygon' object (geonew1) is not iterable,see current solution
      ## shape() returns a new,independent geometry with coords copied from geonew
      ## mapping() returns GeoJSON-like mapping of a geometric object, returns a new geometry with coords copied from 'shape(geonew)'
      ## ["coordinates"] is GeoJSON-like mapping
      geo = mapping(shape(geonew))["coordinates"]
      coordlist = []
      #loop through each polygon 
      for geonew1 in geo:
          ##points = list(geonew1.exterior.coords)
          #loop through each coord
          for coord in geonew1:
              coordlist.append(coord)
      try:
          ## call  make_circle function defined in SEC moudle using coordinate list
          circledef = SEC.make_circle(coordlist)
          ## First create Point object with x, y coordinates of the centroid,
          cp = Point(circledef[0], circledef[1])
          ## buffer the centroid using the radius will create a minimum bounding (or circumscribing)circle!!
          scc = cp.buffer(circledef[2])
          ##compute CIR index
          CIR = geonew.area/scc.area
      except:
          CIR = 0
       
      rec['properties'].update(PARA=p_a)
      rec['properties'].update(ShapeIndex=SI)
      rec['properties'].update(CIRCLE=CIR)
      rec['properties'].update(SCIRCLE=SCIR)

      w.write(rec)
      
      # difference btw smallest circumscribing circle & input polygon

##      try:
##          with fiona.open(diff, 'w', driver=outdiver, crs=outcrs, schema=outschema) as w2:
##              newscc = mapping(shape(scc))
##              for rec in newscc:
##                  w.write(rec)
##              diff = c.difference(newscc)
##      except:
##          print "some failed"
      
##    #Create a shapefile that contains the circles that are the same area as the input
##    #SearchCursor cursor3 is used to read geometry from a copy of "city10",
##    #and then calculate it's area for creating circles of the same area
##    with arcpy.da.SearchCursor(fc3, ["SHAPE@"]) as cursor3:
##        for row in cursor3:
##            cir = cp.buffer((math.sqrt(row[0].area)/math.pi))
##            #insertRow takes A list or tuple of values
##            cursor2.insertRow([cir])
##            print "after print crism"
##
##    del cursor2,cursor3      
