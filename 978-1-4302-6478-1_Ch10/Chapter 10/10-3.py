#=============================
# 10-3.py WeatherUndground Example
#=============================

from xml.etree import ElementTree as ET
import urllib
import sys

class CurrentInfo:
    def getCurrents(self,debuglevel,Location):
        if debuglevel > 0:
            print "Location = %s" % Location
        try:
            CurrentConditions = 'http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=%s' % Location
            urllib.socket.setdefaulttimeout(8)
            usock = urllib.urlopen(CurrentConditions)
            tree = ET.parse(usock)
            usock.close()
        except:
            print 'ERROR - Current Conditions - Could not get information from server...'
            if debuglevel > 0:
                print Location
                sys.exit(1)
        # Get Display Location
        for loc in tree.findall(".//full"):
            self.location = loc.text
        # Get Observation time
        for tim in tree.findall(".//observation_time"):
            self.obtime = tim.text
        # Get Current conditions
        for weather in tree.findall(".//weather"):
            self.we = weather.text
        # Get Temp
        for TempF in tree.findall(".//temperature_string"):
            self.tmpB = TempF.text
        #Get Humidity
        for hum in tree.findall(".//relative_humidity"):
            self.relhum = hum.text
        # Get Wind info
        for windstring in tree.findall(".//wind_string"):
            self.winds = windstring.text
        # Get Barometric Pressure
        for pressure in tree.findall(".//pressure_string"):
            self.baroB = pressure.text

    def output(self):
        print 'Weather Information From Wunderground.com'
        print 'Weather info for %s ' % self.location
        print self.obtime
        print 'Current Weather - %s' % self.we
        print 'Current Temp - %s' % self.tmpB
        print 'Barometric Pressure - %s' % self.baroB
        print 'Relative Humidity - %s' % self.relhum
        print 'Winds %s' % self.winds

    def DoIt(self,Location):
        self.getCurrents(0,Location)
        self.output()

def main():
    location = "80013"
    currents = CurrentInfo()
    currents.DoIt(location)

#===========================================================
# Main loop
#===========================================================
if __name__ == "__main__":
    main()
