"""
Simple demo of a scatter plot.
"""
###This only work in 32 bit IDLE, but won't work in 64-bit IDLE####

import numpy as np
import matplotlib.pyplot as plt
import arcpy

# Calculate Overall lapse rate
elev = arcpy.RasterToNumPyArray(r'C:\Xiaohui\Spatial Programming\w12\week12\edata\elevation.tif')
temp = arcpy.RasterToNumPyArray(r'C:\Xiaohui\Spatial Programming\w12\week12\edata\temperature.tif')

ind = np.where(elev<5000)

flatx = elev[ind]
flaty = temp[ind]

indexes = np.arange(0,len(flatx)-1)
sampleinx = np.random.choice(indexes,10000,replace = False)

x = flatx[sampleinx]
y = flaty[sampleinx]
           
print np.shape(x)

#Calculate Surface lapse rate
lc = arcpy.RasterToNumPyArray(r'C:\Xiaohui\Spatial Programming\w12\week12\edata\current_land_cover.tif')
# find lapse rate only in forested areas (lc<4)
sind = np.where(lc<4)

slx = elev[sind]
sly = temp[sind]

sind2 = np.where(slx <5000)

sx = slx[sind2]
sy = sly[sind2]


# "polyfit" create line to compare with the chart for overall lapse rate
m,b = np.polyfit(x, y, 1)

print m, b, 

results = {}
results['polynomial'] = [m,b]
correlation = np.corrcoef(x, y)[0,1]

print "Overall Correletion is: ", correlation 

plt.scatter(x, y, alpha=0.5)
plt.plot(x, m*x + b, '-')
plt.title(r'Scatter Plot of Overall Lapse Rate')
plt.show()

# 'polyfit' creat line to compare with the chart for forest surface lapse rate
# The 2nd figure will not show until the 1st is closed
sm,sb = np.polyfit(sx, sy, 1)
print sm,sb

s_results = {}
s_results['polynomial'] = [sm,sb]
s_correlation = np.corrcoef(sx, sy)[0,1]

print "Surface Lapse Rate is: ", s_correlation 

plt.scatter(sx, sy, alpha=0.5)
plt.plot(sx, m*sx + sb, '-')
plt.title(r'Scatter Plot of Forest Surface Lapse Rate')
plt.show()
