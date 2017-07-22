# GHY 567L Exercise 5 Xiaohui Liu
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Xiaohui\Spatial Programming\w52\Assign\labData.gdb"
workingDir = r"C:\Xiaohui\Spatial Programming\w52\Assign\\"

#GIS data inputs
taZones = "taZones"
taZonesField = "TAZ"

landUse = "landUse"
luField ="LU_Code"
aField = "Acreage"

census = "censusBlocks"
hhField = "Households"
popField = "Population"
rBOField = "TAZ" 

#text file inputs
landUseM = workingDir + "landUseMultpliers.txt"
rBO = workingDir + "resBuildOut.csv"

#intermediateDataset
outrBO = "rBOData"
cen_j_taz = "cen_j_taz"
lu_j_taz = "lu_j_taz"
cen_summary = "cen_summary"
lu_summary = "lu_summary"

#outputs
outTaz = "outTaz"

arcpy.Copy_management(taZones, outTaz)

# make a copy of the data to be used first before modifying the original
arcpy.CopyRows_management(rBO, outrBO)

# join the buildout data to outTaz
arcpy.JoinField_management(outTaz, taZonesField, outrBO, rBOField)

# spatial join census data with outTaz
arcpy.SpatialJoin_analysis(census, taZones, cen_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

# SUM the population field and housedholds field for census fall within each taZone
arcpy.Statistics_analysis(cen_j_taz, cen_summary, [[popField, "SUM"],[hhField, "SUM"]], taZonesField)

# join the statistics got from last step to outTaz
arcpy.JoinField_management(outTaz, taZonesField, cen_summary, taZonesField)

# add PGM field
arcpy.AddField_management(outTaz, "PGM", "DOUBLE")

# define function for calculating PGM
codeblock = "def findtotal(a,b):\n  if b >0:\n    return a / b\n  else:\n    return 0"

# !SUM_'+popField+'!, !SUM_'+hhField'!
# The above code will only work in file geodatabase, but not on shapefile

arcpy.CalculateField_management(outTaz, "PGM", "findtotal(!SUM_Population!, !SUM_Households!)", "PYTHON_9.3" , codeblock)

#Spatial Join on LandUse with TAZ
arcpy.SpatialJoin_analysis(landUse, taZones, lu_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

# SUM the Acreage field based on each category of taZone and landUse_code
arcpy.Statistics_analysis(lu_j_taz, lu_summary, [[aField, "SUM"]], [taZonesField,luField])

f = open(landUseM, 'r')

for line in f:
    lu = line.strip()
    landUseDataType = lu.split("\t")
    # landUseDataType[0] is the land use type, landUseDataType[1] is the associated multiplier value for each landuse type
    print landUseDataType,landUseDataType[0], landUseDataType[1]

    #each loop creates a landuse summary for a landues type, the summary selects those records with only one landused type (R, LDR,MDR, MHR or AV)
    arcpy.TableSelect_analysis(lu_summary, lu_summary + "_" + landUseDataType[0], luField + " = '" + landUseDataType[0] + "'")

    #Join each landuse summary output back to TazDataset (outTaz), "SUM_Acreage" is the field from the join table to be included from the join,
    #which is created in Statistics_analysis tool before this for loop
    arcpy.JoinField_management(outTaz, taZonesField, lu_summary + "_" + landUseDataType[0], taZonesField, str("SUM_Acreage"))

    #Add the field(s) you need, the fields are the population for each landuse type
    arcpy.AddField_management(outTaz, str(landUseDataType[0]+ "_Pop"), "DOUBLE")
    
    # print to test the multiplication string for muliplying "landUseData[0]" and landUseData[1]
    print "!PGM!*!SUM_Acreage!*!" + landUseDataType[0] + "!*" + landUseDataType[1]
    
    #Calculate The final fields
    arcpy.CalculateField_management(outTaz, str(landUseDataType[0]+ "_Pop"), "!PGM!*!SUM_Acreage!*!" + landUseDataType[0] + "!*" + landUseDataType[1], "PYTHON_9.3")
  

arcpy.AddField_management(outTaz,"Total_Pop", "DOUBLE")
arcpy.CalculateField_management(outTaz, "Total_Pop", '!R_Pop!+!LDR_Pop!+!MDR_Pop!+!HDR_Pop!+!MHR_Pop!+!AV_Pop!', "PYTHON_9.3")
    
f.close()
