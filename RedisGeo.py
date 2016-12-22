from RedisConfig import RedisConfig
import redis
from GeoNameRecord import GeoNameRecord
from GeoHit import GeoHit
import json
from smaz import compress, decompress

import base64
import zlib

class RedisGeo:

    conf = None
    connection = None

    def __init__(self):
        self.conf =  RedisConfig()
        print "Trying to connect to Redis at " + self.conf.host, "Port: " + str(self.conf.port), "DB: " + str(self.conf.db)
        try:
            self.connection = redis.StrictRedis(host=self.conf.host,port=self.conf.port,db=self.conf.db)
            print "Successfully connected to redis"
        except redis.ConnectionError:
            print "Connection Failure"


    def info(self):
        result = self.connection.info()
        print result



    def storeGeoNameRecord(self, georec):

        jsonString = json.dumps(georec.serializeToMap())
        compressedString = zlib.compress(jsonString,9)
        #compressedString = base64.b64encode(compress(jsonString))
        try:
            self.connection.execute_command("GEOADD",self.conf.geoKey,georec.longitude,georec.latitude,compressedString)
        except redis.ResponseError, e:
            print "Could not store record to Redis. Received Response error: "+str(e)

    def getGeoNamesByLocationRadius(self,longitude, latitude, radius, distUnit="km"):
        resultSet = self.connection.execute_command("GEORADIUS",self.conf.geoKey,longitude,latitude,radius,distUnit, "WITHDIST")
        result = []
        for r in resultSet:
            grMap = json.loads(zlib.decompress(r[0])) #first element corresponds to json record
            gr = GeoNameRecord.deserializeMap(grMap)

            hit = GeoHit() #c
            hit.geoRec = gr
            hit.dist = float(r[1]) #second element corresponds to distanc as calculated by redis
            result.append(hit)
        #sort resultset by distance, ascending
        result.sort(key=lambda x: x.dist)
        return result
