
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

# Filename of input file
vector_fn_list = glob.glob(r"C:\data\spa\*new")
print vector_fn_list[:]

##precip_1 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_1_new')
##precip_2 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_2_new')
##precip_3 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_3_new')
##precip_4 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_4_new')
##precip_5 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_5_new')
##precip_6 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_6_new')
##precip_7 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_7_new')
##precip_8 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_8_new')
##precip_9 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_9_new')
##precip_10 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_10_new')
##precip_11 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_11_new')
##precip_12 = gdal.Open(r'C:\Xiaohui\Spatial Programming\w11\week10data\w11\prec_12_new')
##
###convert raster to numpy arrary, get the 1st (also the only, band)
##myarray1 = np.array(precip_1.GetRasterBand(1).ReadAsArray())
##myarray2 = np.array(precip_2.GetRasterBand(1).ReadAsArray())
##myarray3 = np.array(precip_3.GetRasterBand(1).ReadAsArray())
##myarray4 = np.array(precip_4.GetRasterBand(1).ReadAsArray())
##myarray5 = np.array(precip_5.GetRasterBand(1).ReadAsArray())
##myarray6 = np.array(precip_6.GetRasterBand(1).ReadAsArray())
##myarray7 = np.array(precip_7.GetRasterBand(1).ReadAsArray())
##myarray8 = np.array(precip_8.GetRasterBand(1).ReadAsArray())
##myarray9 = np.array(precip_9.GetRasterBand(1).ReadAsArray())
##myarray10 = np.array(precip_10.GetRasterBand(1).ReadAsArray())
##myarray11 = np.array(precip_11.GetRasterBand(1).ReadAsArray())
##myarray12 = np.array(precip_12.GetRasterBand(1).ReadAsArray())
##
#### RuntimeWarning: overflow encountered in add
###new_array1 = myarray1 +myarray2 # +myarray3 +myarray4 +myarray5 +myarray6
###new_array2 = myarray7 +myarray8 +myarray9 +myarray10 +myarray11 +myarray12 
##
##
##
###write manupulated data out
##outBand = output_ds.GetRasterBand(1)
##outBand.WriteArray(myarray1)

