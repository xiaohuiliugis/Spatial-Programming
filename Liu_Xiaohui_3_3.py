import math, urllib

def recalculate_coordinate(val,_as=None):
  """
    Accepts a coordinate as a tuple (degree, minutes, seconds)
    You can give only one of them (e.g. only minutes as a floating point number) and it will be duly
    recalculated into degrees, minutes and seconds.
    Return value can be specified as 'deg', 'min' or 'sec'; default return value is a proper coordinate tuple.
  """
  deg,  min,  sec = val
  # pass outstanding values from right to left
  min = (min or 0) + int(sec) / 60
  sec = sec % 60
  deg = (deg or 0) + int(min) / 60
  min = min % 60
  # pass decimal part from left to right
  dfrac,  dint = math.modf(deg)
  min = min + dfrac * 60
  deg = dint
  mfrac,  mint = math.modf(min)
  sec = sec + mfrac * 60
  min = mint
  if _as:
    sec = sec + min * 60 + deg * 3600
    if _as == 'sec': return sec
    if _as == 'min': return sec / 60
    if _as == 'deg': return sec / 3600
  return deg,  min,  sec
    
def points2distance(slong, slat, elong, elat):
  """
    Calculate distance (in kilometers) between two points given as (long, latt) pairs
    based on Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula).
    slong = Starting Longitude
    slat = Starting Latitude
    elong = ending Longitude
    elat = Ending Latitude
  """
  start = ((slong,0,0),(slat,0,0))
  end = ((elong,0,0),(elat,0,0))
  start_long = math.radians(recalculate_coordinate(start[0],  'deg'))
  start_latt = math.radians(recalculate_coordinate(start[1],  'deg'))
  end_long = math.radians(recalculate_coordinate(end[0],  'deg'))
  end_latt = math.radians(recalculate_coordinate(end[1],  'deg'))
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = math.sin(d_latt/2)**2 + math.cos(start_latt) * math.cos(end_latt) * math.sin(d_long/2)**2
  c = 2 * math.asin(math.sqrt(a))
  return 6371 * c

def getaddresslocation(address):
    params = urllib.urlencode({'address': address})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

def getlocationList(cities):
    listofTupleLocation = []
    for city in cities:
        location = getaddresslocation(city)
        listofTupleLocation.append(location)
    return listofTupleLocation

def countLarge(inputList, largeNumber):

    total_1 = 0
    for value in inputList:
        if (value > largeNumber):
            total_1 = total_1 + 1

    return total_1

#finds the average value of a list (or tuple)
def findStats(*t):
    LargeNumbers = -1
    if (len(t) > 1):
        #find the number of values greater than X
        x = t[1]
        LargeNumbers = countLarge(t[0],x)

    inputList = t[0]
    total = 0
    for value in inputList:
        total = total + value
    mean = float(total) / float(len(inputList))

#This part calculates the St.DEV
    stDev =0
    squareSum = 0.0
    for value in inputList:
        squareSum += ((value-mean)**2)
    division = float(squareSum/float(len(inputList)-1))
    stDev = math.sqrt(division)
    

    if (LargeNumbers > -1):
        return total, mean, stDev,LargeNumbers
    else:
        return total, mean,


cities = ["Hattiesburg, MS", "New York, NY", 'Seattle, WA', "Irvine, CA", "Chicago,IL"]

LLlocations = getlocationList(cities)

# check what is referenced by LLlocations object and its element
print 'The coordinates of the given cities are: ',LLlocations

# total_d is the cumulative sum of the single distances, d_list stores the single distances
total_d =0.0
single_d_list = []
total_d_list = []
for i in range(len(LLlocations)-1):
    x1=LLlocations[i][0]
    y1=LLlocations[i][1]
    x2=LLlocations[i+1][0]
    y2=LLlocations[i+1][1]
    single_d = points2distance(x1,y1,x2,y2)
    total_d += points2distance(x1,y1,x2,y2)
    # append each new 'total distance' to d_list
    single_d_list.append(single_d)
    total_d_list.append(total_d)

print 'The individual distance between cities are :', single_d_list      
print 'The successive cumulative sum of the distances are:', total_d_list   
print 'The total distance of all individual legs is ', total_d
print 'The sum, mean, standard deviation, and the number of individual legs above 3000 are :', findStats(single_d_list,3000)
   
