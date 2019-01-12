from firebase import firebase

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

temp = int(input("Temperature: "))
time = int(input("Time:"))


data={
    'Temperature': temp,
    'Time' : time
}

result = myDBConn.post('/Temperature/', data)

print (result)