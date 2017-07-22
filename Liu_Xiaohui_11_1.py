
from osgeo import gdal, ogr
import numpy as np
import glob
# open up a raster datasets

#Open the land cover Dataset
target_ds = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\current_lc_small.tif')
#get transformation information
geotrans = target_ds.GetGeoTransform()
cols = target_ds.RasterXSize
rows = target_ds.RasterYSize
#create empty dataset
raster_fn = r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\mean_prec.tif'
output_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, cols, rows, 1, gdal.GDT_CFloat64)
output_ds.SetGeoTransform(geotrans)

# Filename of input OGR file
watershed_fn = r'C:\data\spa\tydixton_watershed.shp'
prec_fn_list = glob.glob(r"C:\Xiaohui\Spatial Programming\w11\week10data\w11\*new")

count = 0
arraylist = []
for prec in prec_fn_list:
    ###convert raster to numpy arrary, get the 1st (also the only, band

    prec_tif = gdal.Open(prec)
    # read each precipatation layer and convert to numpy array
    myarray = np.array(prec_tif.GetRasterBand(1).ReadAsArray())
    # make a copy of each array and append to arraylist
    arraylist.append(myarray[:])
    
#create an empty array with the same cellsize as each item in arraylist
totalarray = arraylist[0]*0
for ar in arraylist:
    totalarray = ar + totalarray

#calculate the mean
prec_mean = np.mean(totalarray)


# create an empty tiff to store final mean
output_mean = r'C:\Xiaohui\Spatial Programming\w11\week10data\mean.tif'
output_ds_mean = gdal.GetDriverByName('GTiff').Create(output_mean, cols, rows, 1, gdal.GDT_CFloat64)
output_ds_mean.SetGeoTransform(geotrans)
# get band #
outBand_mean = output_ds_mean.GetRasterBand(1)
#write prec_mean array to output
outBand.WriteArray(prec_mean)
    
