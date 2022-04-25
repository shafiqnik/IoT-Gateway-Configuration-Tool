# FC_Configurator
This application is used for configuring the Minew G1 Gateway
It starts a webserver  and make rest calls to configure the gateway
How to use this tool
Run the fc_auto_configure.py
Open browers and goto localhost:8000/redocs for API documentations
Use a Windows machine and call WifiConnect function, this forces the Windows Machine to connect to ssid of IoT Gateway
(Other Platforms will require manaul connection to wifi network)
After the computer is connected to ssid of IoT Gateway, you can create simple HTML pages to perform configuration of the IoT Gateway
As an example open FC.HTML  goto Step 1  Enter ID of IoT Gateway. 
On Step 2 enter the wifi credentials which the IoT Gatway needs to connect and then click configure.
The tool confiures IoT gateway with host, port number, BLE beacon mac filter.


**This tool is as it is and it is designed to automate configuration of IoT Gateway**
** No warranty is provided **
