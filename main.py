from pynput.keyboard import Key, Controller
import speech_recognition as sr
import subprocess, time
import keyboard
from pywinauto import Application  
import mkj_pkg.main as mkj

keyboardTwo = Controller()
while True:
    while keyboard.is_pressed('ins'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening... ")
            audio = r.listen(source)
            BING_KEY = "901ff8bec4f04c679b9680be6ebf10f0"  #API KEY HERE
            word = r.recognize_bing(audio, key=BING_KEY)
            wordS = word.lower()
            print(wordS)

            # PLAY
            if wordS[0:4] == "play":
                mkj.shortimportant("PLAY WORKING")
                mkj.call("C:\Users\White Lotus\AppData\Roaming\Spotify\Spotify.exe")

            
            # PAUSE
            elif wordS[0:5] == "pause":
                mkj.shortimportant("PAUSE WORKING")
                

            # NEXT
            elif wordS[0:4] == "next":
                mkj.shortimportant("NEXT WORKING")
                mkj.call("C:\Users\White Lotus\AppData\Roaming\Spotify\Spotify.exe")

            # PREVIOUS
            elif wordS[0:8] == "previous":
                mkj.shortimportant("PREVIOUS WORKING")
                mkj.call("C:\Users\White Lotus\AppData\Roaming\Spotify\Spotify.exe")

            # SEARCH
            elif wordS[0:6] == "search": 
                mkj.shortimportant("SEARCH WORKING")
                mkj.call("C:\Users\White Lotus\AppData\Roaming\Spotify\Spotify.exe")

            elif wordS[0:4] == "file":
                print("Flames")