#https://fastapi.tiangolo.com/
#http://localhost:8000/docs

# How to run the code?
# Option 1: RUN fc_auto_configure.py  this file launches the application on port 5000
# Option 2: RUN THE CODE USING THE TERMINAL  "uvicorn main:app --reload" launches application on port 8000


from typing import Optional
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from FixedCollector import FCconfig
from WifiConnect import WifiConnect

app = FastAPI(title = 'Minew G1 Fixed Collector Auto configuration')

fc = FCconfig()
wc = WifiConnect()


class Item(BaseModel):
    name: str
    price: float
    is_offer:Optional[bool] = None

'''
When the method is called via browsers. It connects the laptop to 
access point of the Fixed Collector.
for example:
Use browers to goto http://localhost:8000/ssid/GW-AC233FC079F0
It will connect the laptop to hotspot of Fixed Collector GW-AC233FC079F0
'''

'''

https://fastapi.tiangolo.com/advanced/extending-openapi/

'''
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FX2.0 API Configuration",
        version= "2",
        description="API for auto configuring FX2.0",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://vecima.com/wp-content/uploads/thegem-logos/logo_7e80e19e1dd07cc3d09d9383ab790a6c_2x.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi


@app.get('/ssid/{ssid_name}', tags=['Fixed Collector Wifi Hotspot'])
def wifiConnect(ssid_name: str):
    print('the ssid id is ', ssid_name)
    wc.connectWifi(ssid_name)
    return{'ssid_name':ssid_name}


'''
Setup the wifi credential of Fixed Collector
'''
@app.get('/setwifi/{ssid},{password}')
def setWifi(ssid:str, password:str):
    print('ssid and password is ', ssid,password)
    fc.SetWifi(ssid,password)
    fc.Reboot()
    try:
        return {'wifiset':'true'}
    except Exception:
        print('there was an expection')


'''
Reboots the Fixed collector
'''
@app.get('/reboot')
def reboot():
    fc.Reboot()
    return{'FCReboot':'True'}

'''
Turns the LED On
'''
@app.get('/ledOn')
def LedOn():
    fc.TurnLED('On')
    return{'LEDStatus':'On'}

'''
Turns the LED Off
'''
@app.get('/ledOff')
def LedOff():
    fc.TurnLED('Off')
    return{'LEDStatus':'Off'}


'''
Default page
shows link to documenations
'''
@app.get("/")
def read_root():
    return {'Documentation link http://localhost:8000/redoc'}

#http://localhost:8000/items/1
#output {"item_id":1,"question":null}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "question": q}



@app.post('/mypost/', status_code = 201)
async def create_item(name: str):
    print('your name is ', name)
    return {'name':name}




@app.get("/help/")
async def create_item():
     print('the name of the item is ')
     return {'Please goto this page for all the info http://localhost:8000/redoc'}