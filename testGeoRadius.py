from RedisGeo import RedisGeo
import csv
import GeoNameRecord as gr
import sys
import random
import time

redisGeo =  RedisGeo()
numReq = 100000
resLen = 0.0

testLocs = redisGeo.getGeoNamesByLocationRadius(6.113548278808594, 50.78675130773451,15)
for a in testLocs:
    print a.geoRec.name, a.dist
    
print "Now we make "+str(numReq)+" random lookups with 5km radius"
start_time = time.time()

for i in range(0,numReq):
    latitude = random.uniform(30,50)
    longitude = random.uniform(5,15)
    testLocs = redisGeo.getGeoNamesByLocationRadius(longitude,latitude,5)
    resLen = resLen+len(testLocs)

end_time = time.time()

delta = end_time - start_time

print "Total: " + str(delta) + "s"
perSec = numReq / delta
print "Throughput: " + str(perSec)+ " lookups/s"
avgResSize = resLen/numReq
print "Avg. len of result set: " + str(avgResSize)
