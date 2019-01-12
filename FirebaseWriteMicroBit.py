from firebase import firebase
import datetime
from time import sleep
import serial

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        data = str(s.readline(2))
        data = data.replace("b","")
        data = data.replace("'","")
        data = data.replace(" ","")
        temp = int(data)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        currentdate = datetime.datetime.now().strftime("%d/%m/%Y")
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        
        data={
            'Temperature': temp,
            'TimeStamp' : timestamp,
            'Time' : currenttime,
            'Date' : currentdate
        }

        result = myDBConn.post('/Temperature/', data)

        sleep(180)

        
      
finally:
    s.close()