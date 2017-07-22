
import arcpy

rows = arcpy.da.SearchCursor(r"C:\Xiaohui\Spatial Programming\w7\data\GPS_points.shp", ["SHAPE@XY","Animal","Time"])
lines = arcpy.da.InsertCursor(r"C:\Xiaohui\Spatial Programming\w7\data\tracks.shp",["SHAPE@","Time","Animal"])

totalx =0
totaly =0
count =0
animals=[]
for row in rows:
    #cAnimal = str(row[1])
    print "Animal:" + str(row[1])
    animals.append(row[1])
    #total+=row[0]
    
    totalx += row[0][0]
    totalx += row[0][1]
    count +=1
    
uAnimals=set(animals)
print uAnimals
centroid = totalx/count, totaly/count
print centroid


del rows,lines

