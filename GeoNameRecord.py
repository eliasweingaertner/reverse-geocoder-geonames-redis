
class GeoNameRecord():
    
    geonameid = ""
    name = ""
    asciiname = ""
    alternatenames = ""
    latitude = 0.0
    longitude = 0.0
    feature_class = ""
    feature_code = ""
    country_code = ""
    cc2 = ""
    admin1 = ""
    admin2 = ""
    admin3 = ""
    admin4 = ""
    population =""
    elevation = ""
    dem = ""
    timezone = ""
    modification_date = ""

    @staticmethod
    def parseTSV2GeoNameRecord(csvRow):
        elements = csvRow
        gr = GeoNameRecord()
        gr.geonameid = elements[0]
        gr.name = elements[1]
        gr.asciiname = elements[2]
        gr.alternatenames = elements[3]    
        gr.latitude = float(elements[4])
        gr.longitude = float(elements[5])
        gr.feature_class = elements[6]
        gr.feature_code = elements[7]
        gr.country_code = elements[8]
        gr.cc2 = elements[9]
        gr.admin1 = elements[10]
        gr.admin2 = elements[11]
        gr.admin3 = elements[12]
        gr.admin4 = elements[13]
        gr.population = elements[14]
        gr.elevation = elements[15]
        gr.dem = elements[16]
        gr.timezone = elements[17]
        gr.modification_date = elements[18]
        return gr
    
    def serializeToMap(self):
        result = {"gid":self.geonameid,"n":self.name,
                  "a2name":self.asciiname,"ans":self.alternatenames,
                  "lat":self.latitude,"lon":self.longitude,
                  "fcl":self.feature_class,"fc":self.feature_code,
                  "cc":self.country_code,"cc2":self.cc2,
                  "a1":self.admin1,"a2":self.admin2,"a3":self.admin3,"a4":self.admin4,
                  "p":self.population,"el":self.elevation,"dem":self.dem,
                  "tz":self.timezone,"md":self.modification_date}
        return result
    
                    
    @staticmethod
    def deserializeMap(datamap):
        
        elements = datamap
        gr =  GeoNameRecord()
        gr.geonameid = elements["gid"]
        gr.name = elements["n"]
        gr.asciiname = elements["a2name"]
        gr.alternatenames = elements["ans"]    
        gr.latitude = float(elements["lat"])
        gr.longitude = float(elements["lon"])
        gr.feature_class = elements["fcl"]
        gr.feature_code = elements["fc"]
        gr.country_code = elements["cc"]
        gr.cc2 = elements["cc2"]
        gr.admin1 = elements["a1"]
        gr.admin2 = elements["a2"]
        gr.admin3 = elements["a3"]
        gr.admin4 = elements["a4"]
        gr.population = elements["p"]
        gr.elevation = elements["el"]
        gr.dem = elements["dem"]
        gr.timezone = elements["tz"]
        gr.modification_date = elements["md"]
        
        return gr      
 
