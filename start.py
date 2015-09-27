import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
volume=engine.getProperty('volume')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_10.0')
engine.say('HELLO MISTER KARAN PATHAK . HOW ARE YOU THIS LOVELY DAY')

engine.runAndWait()

engine.say('PLEASE GIVE YOUR CHOICE')
engine.runAndWait()


w=""
try:
    while w!="shut up":
         engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_10.0')
         import pyaudio
         import speech_recognition as sr
         print "karan"
         r = sr.Recognizer()
         with sr.Microphone() as source:                
                 audio = r.listen(source)                
         print ("processing....")
         try:
            w=r.recognize(audio)
            if w=="1" :
                fo = open("H:\work.txt", "r+")
                line = fo.read();
                print  (line)
                fo.close()
                engine.say(line)
                engine.runAndWait()
         except LookupError:
                print("Could not understand audio")
         if w!="shut up":
             engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_10.0') 
             engine.say('SIR PLEASE GIVE YOUR CHOICE')
             engine.runAndWait()
         print ("wait ....")
except SystemExit:
    print ("karan")
engine.say('ENJOY YOUR DAY MISTER KARAN PATHAK')
engine.runAndWait()


