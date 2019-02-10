
myDBConn = firebase.FirebaseApplication('https://davidstempmonitor.firebaseio.com/', None)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "/dev/ttyS0"
ser.open()

while True:
    data = ""
    while data == "":
        data = str(ser.readline())
    
    
    
    final = data[2:]
    final = final.replace(" ","")
    final = final.replace("\\r\\n","")
    final = final.replace("'","")
    
    print(final)
    
    senddata = {
        'State' : final
    }
    
    result = myDBConn.delete('/RemoteControl/', None)
    result = myDBConn.post('/RemoteControl/', senddata)
    
    time.sleep(5)
    
ser.close()
