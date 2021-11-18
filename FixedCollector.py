import requests

class FCconfig:

    def __init__(self):
        self.url = 'http://192.168.99.1/'
        self.payload = {}
        self.headers = {}


    #Invokes Scan Method of FixedCollector and retuns list of available WIFI
    def getWifi(self):
        wifi = 'cgi-bin/aps'

        response = requests.request("GET", self.url+wifi, headers=self.headers, data=self.payload)
        print(response.text)


    #Queries Fixed Collector for all Parameters and returns All Parameters
    def getAllParam(self):

        AllParam = "cgi-bin/checkparam"
        response = requests.request("GET", self.url + AllParam , headers=self.headers, data=self.payload)
        print(response.text)

    #This Function takes one parameter On or Off to turn the LED of Fixed Collctor On or Off
    def TurnLED(self,Status):

        LED = "cgi-bin/setleds"
    #payload = {"action":"config","takeEffectImmediately":"YES","common":{"isLongBright":"NO"}}
        LedOff= 'isLongBright=YES&disableLED=YES'
        LedOn = 'isLongBright=YES&disableLED=NO'

        if Status == 'On':
            print('status is On')
            r = requests.get(self.url + LED, params=LedOn)
        else:
            print('status is Not On')
            r = requests.get(self.url + LED, params=LedOff)
        print(r.text)

    def SetWifi(self,ssid, password):
        self.ssid = ssid
        self.password = password
        #wifiCredential = "ssid=SHAW-SA-2.4G&password=2511510A8392SA&repeaterMode=dhcp&ipaddr=192.168.0.3&netmask=255.255.255.0&gateway=192.168.0.1&dns1=114.114.114.114&dns2=8.8.8.8"

        #FX3.0
        wifiCredential ="ssid={}&bssid=&encryption=psk-mixed&cipher=auto&key={}&keyi=1&key1=&key2=&key3=&key4=&eap_type=tls&priv_key_pwd=&auth=PAP&priv_key2_pwd=&identity=&anonymous_identity=&password=&repeaterMode=dhcp&ipaddr=192.168.0.3&netmask=255.255.255.0&gateway=192.168.0.1&dns1=114.114.114.114&dns2=8.8.8.8&reverted=NO&net_profile=GuestWifi&net_hidden=&net_check=".format(ssid,password)

        #FX2.0  setting ->
        #wifiCredential = "ssid={}&password={}&repeaterMode=dhcp&ipaddr=192.168.0.3&netmask=255.255.255.0&gateway=192.168.0.1&dns1=114.114.114.114&dns2=8.8.8.8".format(ssid,password)

        setRepeater = 'cgi-bin/setrepeater'
        r = requests.get(self.url + setRepeater, params=wifiCredential)
        print('wifi credentials were correctly setup')
        print(r.text)


    def Reboot(self):
        reboot = 'cgi-bin/reboot'
        r = requests.get(self.url + reboot)



#fc = FCconfig()
#fc.getWifi()

#getWifi()
#getAllParam()
#SetWifi()
#TurnLED('On')
#Reboot()
