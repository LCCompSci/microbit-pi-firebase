from firebase import firebase
import datetime

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

temp = int(input("Temperature: "))
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

print (result)