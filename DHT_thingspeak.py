from machine import Pin, ADC
import time
import network
import urequests

ssid= "0123456789"
pas= "0123456789"

pump= Pin(4)
mannu= ADC(Pin (26))
mannu_limit= 30000
tsecond= 30
cid= 2524018
api= '************'

def connect(ssid,pas):
    wlan= network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        wlan.connect(ssid, pas)
        
while True:
    connect(ssid, pas)
    
    mannu_val= mannu.read_u16()
    
    f_1= mannu_val
    
    url = 'https://api.thingspeak.com/update?api_key=3CSIK649X18BUBW9&field1=' + str(f_1)
    response = urequests.get(url)
    print(response)
    time.sleep(15)
    
    
    
    print("mannu\t",mannu_val)
    time.sleep(1)
    
    if mannu_val >= mannu_limit:
        temp= tsecond
        while temp>0 :
            temp-=1
            pump.on()
            time.sleep(1)
        
    else:
        pump.off()
        
    #time.sleep(10)
