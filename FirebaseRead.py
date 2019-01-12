from firebase import firebase

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

myGetResults = myDBConn.get('/Temperature/',None)

print(myGetResults)

for keyID in myGetResults:
    print (keyID, "\t", myGetResults[keyID]['Temperature'], myGetResults[keyID]['Time'])