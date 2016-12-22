#!/usr/bin/python
from RedisGeo import RedisGeo
import csv
import GeoNameRecord as gr
import sys
import getopt
from twisted.python.test.test_deprecate import ImportedModuleAttributeTests

csv.field_size_limit(sys.maxsize)
redisGeo =  RedisGeo()

filename=sys.argv[1]


k=0
with open(filename) as tsv:
    print "Importing files from GEONAMES dump file: "+filename
    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
        geoRecord = gr.GeoNameRecord.parseTSV2GeoNameRecord(line)
        #print "Storing "+geoRecord.name
        redisGeo.storeGeoNameRecord(geoRecord)
        if (k%1000==0):
            print str(k)+ " records imported"
            
        k=k+1

print "Successfully imported " + str(k)+ " records"