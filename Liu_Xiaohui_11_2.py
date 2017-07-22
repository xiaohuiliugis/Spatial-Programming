from osgeo import gdal, ogr
import numpy as np
import glob
import scipy

# Define pixel_size and NoData value of new raster
pixel_size = 25
NoData_value = -9999

# Filename of input OGR file
watershed_fn = r'C:\Xiaohui\Spatial Programming\w11\week10data\tydixton_watershed.shp'
vector_fn_list = glob.glob(r"C:\Xiaohui\Spatial Programming\w11\week10data\risk*.shp")

# Filename of the raster Tiff that will be created
raster_fn = r'C:\Xiaohui\Spatial Programming\w11\week10data\risk_dataset.tif'
raster2_fn = r'C:\Xiaohui\Spatial Programming\w11\week10data\risk_distance.tif'

# Open watershed data and read extent
watershed_ds = ogr.Open(watershed_fn)
watershed_layer = watershed_ds.GetLayer()
x_min, x_max, y_min, y_max = watershed_layer.GetExtent()

print watershed_layer.GetExtent()

#looped
arraylist = []

for vector_fn in vector_fn_list:
    # Open the data source
    source_ds = ogr.Open(vector_fn)
    source_layer = source_ds.GetLayer()

    ### Create the destination data source
    x_res = int((x_max - x_min) / pixel_size)
    y_res = int((y_max - y_min) / pixel_size)

    ###Create a new raster w/ variable name 'raster_fn' and 2 bands to save rasterized vector layers
    target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
    target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
    band = target_ds.GetRasterBand(1)
    band.SetNoDataValue(NoData_value)


    ###Create a new raster w/ variable name 'raster2_fn' and 2 bands to save the proximity created from 'raster_fn'
    target2_ds = gdal.GetDriverByName('GTiff').Create(raster2_fn, x_res, y_res, 2, gdal.GDT_Int16)
    ### Set the extent and cell 
    target2_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

    ### Rasterize the vector layer in the directory, then save to 'target_ds'
    gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

    ################## 3rd Part: create proximity dataset  ################################

    ##
    srcband = target_ds.GetRasterBand(1)
    dstband = target2_ds.GetRasterBand(1)
    ## use target_ds layer to compute proximity and saves to target2_ds layer
    gdal.ComputeProximity(srcband, dstband)
    ##
    ###Convert to Array
    myarray = np.array(target2_ds.GetRasterBand(1).ReadAsArray())

    newarray = 500 - myarray

    outputar = np.where(newarray < 0, 0, newarray)
    
    #################### Important trick Here###################################
    #each time through the loop, 'outputar' will be replaced by new array, so
    #use [:] to get a copy of the 'outputar' and append it to 'arraylist'
    # so 'arraylist' keeps a copy of each array each time through the loop
    arraylist.append(outputar[:])
    print np.max(outputar)

    # save the output each time, but will be replace the next time
    outBand = target2_ds.GetRasterBand(2)
    outBand.WriteArray(outputar)
# create an empty array to save the array output from above
totalarray = arraylist[0] * 0
for ar in arraylist:
    totalarray = ar + totalarray[:]
    print ar

print totalarray

#create empty dataset for saving the total
ras_tot_fn = r'C:\Xiaohui\Spatial Programming\w11\week10data\total.tif'
out_tot_ds = gdal.GetDriverByName('GTiff').Create(ras_tot_fn, x_res, y_res, 2, gdal.GDT_Int16)
out_tot_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

#write manupulated data out
outBand = out_tot_ds.GetRasterBand(2)
outBand.WriteArray(totalarray)

################################################################
######## dataset needs to be set to None so it will be save on disk
################################################################
source_ds = None
target_ds = None
target2_ds = None
##target3_ds = None
