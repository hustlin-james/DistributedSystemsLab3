import zeep
import datetime
import xmltodict


#https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?lat=38.99&lon=-77.01&product=time-series&startTime=&endTime=&maxt=maxt&mint=mint&wspd=wspd&wdir=wdir

def main():
    wsdl = 'https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl'
    client = zeep.Client(wsdl=wsdl)

    startTime = datetime.datetime.now()
    endTime = datetime.datetime.now()
    weatherParameters = {
        'maxt':True,
        'mint':True,
        'temp':True,
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
    Unit = "e"

    #32.9108,-96.6293
    result = client.service.NDFDgen(latitude=32.9108,longitude=-96.6293,product='time-series',startTime=startTime, endTime=endTime,Unit=Unit,weatherParameters=weatherParameters)
    doc = xmltodict.parse(result)

    print(result)


    maxTempVal = doc['dwml']['data']['parameters']['temperature'][0]['value']

    minTempVal = doc['dwml']['data']['parameters']['temperature'][1]['value']

    windSpeedVal = doc['dwml']['data']['parameters']['wind-speed'][0]['value']
    windDirectionVal= doc['dwml']['data']['parameters']['direction']['value']

    print(maxTempVal)
    print(minTempVal)
    print(windSpeedVal)
    print(windDirectionVal)

    # windSpeedAry = doc['dwml']['data']['parameters']['wind-speed'][0]['value']
    # windSpeedValues = ",".join(windSpeedAry)

    # windDirectionAry = doc['dwml']['data']['parameters']['direction'][1]['value']
    # windDirectionValues = ",".join(windDirectionAry)


if __name__ == "__main__":
    main()