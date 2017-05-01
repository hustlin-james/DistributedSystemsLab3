import Tkinter as tk
import requests
import xmltodict

# Include at least four of the following variables in your display: Maximum Temperature,
# Minimum Temperature, Dew point Temperature, 12 Hour Probability of Precipitation,
# Cloud Cover Amount, Wind Speed, Wind Direction, Weather Icons, Wave Height.

#https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?lat=38.99&lon=-77.01&product=time-series&startTime=&endTime=&maxt=maxt&mint=mint&wspd=wspd&wdir=wdir

class App:
    def __init__(self,master):
        frame = tk.Frame(master)
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
        self.windSpeedLbl = tk.Label(frame,textvariable=self.windSpeedVar,width=150)
        self.windSpeedLbl.pack()

        self.windDirectionTitleLbl = tk.Label(frame,text="Wind Direction")
        self.windDirectionTitleLbl.pack()

        self.windDirectionVar = tk.StringVar()
        self.windDirectionVar.set("NA")
        self.windDirectionLbl = tk.Label(frame,textvariable=self.windDirectionVar)
        self.windDirectionLbl.pack()

        self.coordinateEntryLbl = tk.Label(frame,text="Enter Latitude and Longitude.  (Lat,Long)")
        self.coordinateEntryLbl.pack()

        self.coordinateEntry = tk.Entry(frame)
        self.coordinateEntry.pack()
            
        self.getWeatherBtn = tk.Button(frame, text='Get Weather', width=50, command=self.get_weather)
        self.getWeatherBtn.pack()
    
    def get_weather(self):
        #38.99,-77.01
        coords = self.coordinateEntry.get().split(",")
        lat = coords[0]
        lon = coords[1]
        params = {
            'lat':lat,
            'lon':lon,
            'product':'time-series',
            'startTime':'',
            'endTime':'',
            'maxt':'maxt',
            'mint':'mint',
            'wspd':'wspd',
            'wdir':'wdir'
        }
        r = requests.get('https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php', params = params)
        doc = xmltodict.parse(r.text)
        maxTempAry = doc['dwml']['data']['parameters']['temperature'][0]['value']
        maxTempValues = ",".join(maxTempAry)

        minTempAry = doc['dwml']['data']['parameters']['temperature'][1]['value']
        minTempValues = ",".join(minTempAry)

        windSpeedAry = doc['dwml']['data']['parameters']['wind-speed']['value']
        windSpeedValues = ",".join(windSpeedAry)

        windDirectionAry = doc['dwml']['data']['parameters']['direction']['value']
        windDirectionValues = ",".join(windDirectionAry)

        self.maxTemperatureVar.set(maxTempValues)
        self.minTemperatureVar.set(minTempValues)
        self.windSpeedVar.set(windSpeedValues)
        self.windDirectionVar.set(windDirectionValues)

def main():
    root = tk.Tk()
    root.title("Weather App")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()