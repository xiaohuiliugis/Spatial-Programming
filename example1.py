import fiona

c = fiona.open(r'C:\Xiaohui\Spatial Programming\w9\data\GPS_points.shp', 'r')

print c.crs
print c.schema

for rec in c:
    print rec
