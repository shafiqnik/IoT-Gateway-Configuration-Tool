'''
Scans wifi networks and then connects to Fixed Collector Wifi Hotspot network
'''

import os
import re
import subprocess, sys

class WifiConnect:

    def __init__(self):
        self.command = 'cmd /c "netsh wlan show networks'

    def availableNetworks(self):
        print('showing available networks')
        subprocess.call(self.command)

    def connectWifi(self, issid):
        self.issid = issid
        os.system(f'''cmd /c "netsh wlan connect name = {issid}"''')
        print('if you are not yet connected, try connecting to previous ssid again....')


