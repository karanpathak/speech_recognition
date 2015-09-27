import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
volume=engine.getProperty('volume')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_10.0')
engine.say('HELLO MISTER KARAN PATHAK . TEST BEFORE SHUTDOWN')
engine.runAndWait()

engine.say('PLEASE GIVE YOUR CHOICE')
engine.runAndWait()

w=""
try:
    while w!="shut up":
    
         import pyaudio
         import speech_recognition as sr
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)                
         
         try:
            print "processing...."
            w=r.recognize(audio)
            if "1" in w :
                from os import system
                system("H:\work.txt")
                engine.say('60 SECONDS BEFORE SHUTDOWN')
                engine.runAndWait()
                system("shutdown /s /t 60")
                system("cmd")
                break
         except LookupError:
                print("SORRY SIR Could not understand audio")
                engine.say('SIR PLEASE GIVE YOUR CHOICE AGAIN')
                engine.runAndWait()

         print "wait ...."
except SystemExit:
    print "karan"
engine.say('ENJOY YOUR DAY MISTER KARAN PATHAK')
engine.runAndWait()
