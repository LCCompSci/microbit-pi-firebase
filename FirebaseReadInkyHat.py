from firebase import firebase
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from inky import InkyPHAT
import time



mostrecentkeyID = 0
mostrecentTimestamp = 0

myDBConn = firebase.FirebaseApplication('https://pifirebase-pajo.firebaseio.com/', None)

while True:
    myGetResults = myDBConn.get('/Temperature/',None)

    for keyID in myGetResults:
        if int(myGetResults[keyID]['TimeStamp']) > mostrecentTimestamp:
            mostrecentTimestamp = int(myGetResults[keyID]['TimeStamp'])
            mostrecentkeyID = myGetResults[keyID]
        
    inky_display = InkyPHAT("yellow")
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FredokaOne, 22)



    latestTemp = mostrecentkeyID['Temperature']
    latestTime = mostrecentkeyID['Time']
    latestDate = mostrecentkeyID['Date']
    print("Temperature:",latestTemp)
    print("Temperature:",latestTime)
    print("Temperature:",latestDate)

    message = "Temp: " + str(latestTemp)
    message2 = "Time: " + str(latestTime)
    message3 = "Date: " + str(latestDate)

    w, h = font.getsize(message)
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = (inky_display.HEIGHT / 2) - (h / 2)

    for y in range(0, inky_display.HEIGHT):
        for x in range(0, inky_display.WIDTH):
            img.putpixel((x, y), inky_display.BLACK)
        
    draw.text((0,0),message, inky_display.WHITE, font)
    draw.text((0,h+5),message2, inky_display.YELLOW, font)
    draw.text((0,2*h+10),message3, inky_display.YELLOW, font)
    inky_display.set_image(img)
    inky_display.show()
    time.sleep(180)