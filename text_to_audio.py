from gtts import gTTS
import os
class toAudio:
    mytext=input("Enter text: ")
    language='en'
    myvoice=gTTS(text=mytext,lang=language,slow=False)
    myvoice.save('audioout.mp3')
    os.system("audioout.mp3")

x1 = toAudio()
x1.mytext
