import Tkinter as tk
import requests
import xmltodict
import zeep
import datetime

#James Fielder
#1000631384

# Include at least four of the following variables in your display: Maximum Temperature,
# Minimum Temperature, Dew point Temperature, 12 Hour Probability of Precipitation,
# Cloud Cover Amount, Wind Speed, Wind Direction, Weather Icons, Wave Height.

#https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?lat=38.99&lon=-77.01&product=time-series&startTime=&endTime=&maxt=maxt&mint=mint&wspd=wspd&wdir=wdir


#Input: None
#Output: None
#Summary: A wrapper class for the GUI and variables.
class App:
    #Input: None
    #Output: None
    #Summary: Initialize the GUI and Variables
    def __init__(self,master):
        frame = tk.Frame(master,width=150)
        frame.pack()

        self.maxTemperatureTitleLbl = tk.Label(frame,text="Max Temperature")
        self.maxTemperatureTitleLbl.pack()

        self.maxTemperatureVar = tk.StringVar()
        self.maxTemperatureVar.set("NA")
        self.maxTemperatureLbl = tk.Label(frame,textvariable=self.maxTemperatureVar)
        self.maxTemperatureLbl.pack()
        
        self.minTemperatureTitleLbl = tk.Label(frame,text="Min Temperature")
        self.minTemperatureTitleLbl.pack()

        self.minTemperatureVar = tk.StringVar()
        self.minTemperatureVar.set("NA")
        self.minTemperatureLbl = tk.Label(frame,textvariable=self.minTemperatureVar)
        self.minTemperatureLbl.pack()

        self.windSpeedTitleLbl = tk.Label(frame,text="Wind Speed")
        self.windSpeedTitleLbl.pack()

        self.windSpeedVar = tk.StringVar()
        self.windSpeedVar.set("NA")
        self.windSpeedLbl = tk.Label(frame,textvariable=self.windSpeedVar,width=100)
        self.windSpeedLbl.pack()

        self.windDirectionTitleLbl = tk.Label(frame,text="Wind Direction")
        self.windDirectionTitleLbl.pack()

        self.windDirectionVar = tk.StringVar()
        self.windDirectionVar.set("NA")
        self.windDirectionLbl = tk.Label(frame,textvariable=self.windDirectionVar)
        self.windDirectionLbl.pack()

        self.coordinateEntryLbl = tk.Label(frame,text="Enter Latitude and Longitude.  (Lat,Long)")
        self.coordinateEntryLbl.pack()

        self.coordinateEntryVar = tk.StringVar()
        self.coordinateEntryVar.set('32.9108,-96.6293')
        self.coordinateEntry = tk.Entry(frame,textvariable=self.coordinateEntryVar)
        self.coordinateEntry.pack()
            
        self.getWeatherBtn = tk.Button(frame, text='Get Weather', width=50, command=self.get_weather)
        self.getWeatherBtn.pack()
    #Input: None
    #Output: None
    #Summary: Calls the webservice using Zeep.  First load the wsdl then call 
    #the functions that are attached and pass in the required parameters, then
    #use xmltodict library to parse the XML and get the max,min temperature values
    #and wind speed and wind direction
    def get_weather(self):
        #32.9108,-96.6293
        coords = self.coordinateEntryVar.get().split(",")
        lat = coords[0]
        lon = coords[1]

        wsdl = 'https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl'
        client = zeep.Client(wsdl=wsdl)

        startTime = datetime.datetime.now()
        endTime = datetime.datetime.now() 
        Unit = "e"
        result = client.service.NDFDgen(latitude=float(lat),longitude=float(lon),product='time-series',startTime=startTime, endTime=endTime,Unit=Unit,weatherParameters=weatherParameters)
       
        doc = xmltodict.parse(result)
       
        maxTempVal = doc['dwml']['data']['parameters']['temperature'][0]['value']

        minTempVal = doc['dwml']['data']['parameters']['temperature'][1]['value']

        windSpeedVal = doc['dwml']['data']['parameters']['wind-speed'][0]['value']
        windDirectionVal= doc['dwml']['data']['parameters']['direction']['value']

        self.maxTemperatureVar.set(maxTempVal)
        self.minTemperatureVar.set(minTempVal)
        self.windSpeedVar.set(windSpeedVal)
        self.windDirectionVar.set(windDirectionVal)
#Input: None
#Output: None
#Summary: main function intilizes the weather parameters to specify which values to get,and start the GUI.
def main():
    global weatherParameters
    weatherParameters = {
        'maxt':True,
        'mint':True,
        'temp':False,
        'dew':False,
        'appt':False,
        'pop12':False,
        'qpf':False,
        'sky':False,
        'snow':False,
        'rh':False,
        'wspd':True,
        'wdir':True,
        'wx':False,
        'icons':False,
        'waveh':False,
        'incw34':False,
        'incw50':False,
        'incw64':False,
        'cumw34':False,
        'cumw50':False,
        'cumw64':False,
        'wgust':False,
        'critfireo':False,
        'dryfireo':False,
        'conhazo':False,
        'ptornado':False,
        'phail':False,
        'ptstmwinds':False,
        'pxtornado':False,
        'pxhail':False,
        'pxtstmwinds':False,
        'ptotsvrtstm':False,
        'pxtotsvrtstm':False,
        'tmpabv14d':False,
        'tmpblw14d':False,
        'tmpabv30d':False,
        'tmpblw30d':False,
        'tmpabv90d':False,
        'tmpblw90d':False,
        'prcpabv14d':False,
        'prcpblw14d':False,
        'prcpabv30d':False,
        'prcpblw30d':False,
        'prcpabv90d':False,
        'prcpblw90d':False,
        'precipa_r':False,
        'sky_r':False,
        'td_r':False,
        'temp_r':False,
        'wdir_r':False,
        'wspd_r':False,
        'wwa':False,
        'iceaccum':False,
        'maxrh':False,
        'minrh':False
    }
    root = tk.Tk()
    root.title("Weather App")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()