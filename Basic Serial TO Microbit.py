import datetime
import time
import serial
from firebase import firebase

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'
ser.open()

while True:
    datatosend="test"
    ser.write(datatosend.encode('UTF-8')+ b"\n")
    print ("Write Complete")
    time.sleep(5)
    
ser.close()
