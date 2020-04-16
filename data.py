class Location:
    def __init__(self, locationName=None, lat=None, lon=None, stationId=None, time=None, weatherElement=None):
        self.locationName = locationName
        self.lat = lat
        self.lon = lon
        self.stationId = stationId
        self.time = time
        self.weatherElement = weatherElement

    def from_json(self,json_data):
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.locationName = json_data.get('locationName')
        self.stationId = json_data.get('stationId')
        self.time = json_data.get('time').get('obsTime')

        self.weatherElement = WeatherElement()
        self.weatherElement.from_json(json_data['weatherElement'])
class WeatherElement:
    def __init__(self, wdir=None,wdsd=None,temp=None,humd=None,h24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h24r = h24r

    def from_json(self,json_data):
        for element in json_data:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')
        if element_name == 'WDIR':
            self.wdir = element_value
        if element_name == 'WDSD':
            self.wdsd = element_value
        if element_name == 'TEMP':
            self.temp = element_value
        if element_name == 'HUMD':
            self.humd = element_value
        if element_name == '24R':
            self.h24r = element_value