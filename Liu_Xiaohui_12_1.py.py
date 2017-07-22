"""
Demo of the histogram (hist) function with a few features.

In addition to the basic histogram, this demo shows a few optional features:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the integral of
      the histogram is 1. The resulting histogram is a probability density.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).

"""
## Create a histogram of CIRCLE index from Lab 8 (metrics of shape for cities of mississippi) 
import arcpy
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

array = arcpy.da.FeatureClassToNumPyArray(r'C:\Xiaohui\Spatial Programming\w12\w8\Sub\City10Sub_copy.shp',['CIRCLE'])
x =[]
for a in array:
    x.append(a[0])
    
# example data
#mu = np.mean(a) is mean of distribution
mu =np.mean(x)
# standard deviation of distribution
sigma = np.std(x)

# Return a sample (or samples) from the “standard normal” distribution.
#x = mu + sigma * np.random.randn(1000)
print "List X is :", x

## making chart, bins is the # of bars
num_bins = 20
# the histogram of the data, "normed=1" means the bars are normalized and values add
# up to 1; alpha means transparency
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
print "n is: ", n
print "length of n is: ", len(n)
print "patches is :", patches
print "length of patches is: ",len(patches)
print "mu is:", mu, "sigma is :",sigma
# add a 'best fit' line, is dashed line, tries compares the normal distribution to actural data
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title(r'Histogram of CIRCLE Metrics: $\mu=' + str(mu)+ '$, $\sigma=' + str(sigma)+'$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
#plt.savefig(r'C:\Xiaohui\Spatial Programming\w12\week12\histo.png')
