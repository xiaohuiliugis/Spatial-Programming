# Lab Assignment 4 by Xiaohui Liu

import math, urllib,os

def getaddresslocation(address):
    params = urllib.urlencode({'address': address})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

##if __name__ == "__main__":
##    print getaddresslocation("Hattiesburg, MS")

def getFileList(path):
    f = open(path, "r")
    f.readline()
    fileList = []
    for line in f:
        fileList.append(line.strip())
    f.close()
    return fileList

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

def makeCitiesDict(citiesList):
    CitiesDict = dict()
    for city in citiesList:
        latlog = getaddresslocation(city)
        x = latlog[0]
        y = latlog[1]
        CitiesDict[city] = Point(x, y)
    return CitiesDict

def writeDictFile(aDict, filepath):
    f = open(filepath,"w")
    for item in aDict:
              
        # .x will output the x coordinate
        lat = aDict[item].x
        log = aDict[item].y
        
        f.write(os.linesep + item + " "),
        f.write(str(lat)+ " "),
        f.write(str(log))
 
myCities = getFileList(r"C:\Xiaohui\Spatial Programming\w4\citiesLittle.txt")

myCitiesDict = makeCitiesDict(myCities)
writeDictFile(myCitiesDict,r"C:\Xiaohui\Spatial Programming\w4\Assgn4.txt")

for item in myCitiesDict:
    print item, myCitiesDict[item].x, myCitiesDict[item].y


