from firebase import firebase
mostrecentkeyID = 0
mostrecentTimestamp = 0

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

myGetResults = myDBConn.get('/Temperature/',None)

for keyID in myGetResults:
    if int(myGetResults[keyID]['TimeStamp']) > mostrecentTimestamp:
        mostrecentTimestamp = int(myGetResults[keyID]['TimeStamp'])
        mostrecentkeyID = myGetResults[keyID]
        

print("Temperature:",mostrecentkeyID['Temperature'])
print("Time:",mostrecentkeyID['Time'])
print("Time:",mostrecentkeyID['Date'])