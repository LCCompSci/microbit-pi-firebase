import datetime
import time
import serial
from firebase import firebase

myDBConn = firebase.FirebaseApplication('https://davidstempmonitor.firebaseio.com/', None)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM4'
ser.open()

while True:

    data = str(ser.readline())
    final = data[2:]
    final = final.replace(" ","")
    final = final.replace("\\r\\n","")
    final = final.replace("'","")
    
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
   
    
    data = {
        'Temp' : final,
        'Time' : now
    }
    
    result = myDBConn.post('/MyTemperature/', data)
    
    time.sleep(5)
    
ser.close()
