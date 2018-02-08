from pynput.keyboard import Key, Controller
import speech_recognition as sr
import subprocess, time, webbrowser, keyboard, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pywinauto import Application  
import mkj_pkg.main as mkj

if os.name == "nt":
    commandOne = 'cls'
else:
    commandOne = 'clear'
    os.system(commandOne)

browser = webdriver.Firefox()

keyboardTwo = Controller()
while True:
    if os.name == "nt":
        commandOne = 'cls'
    else:
        commandOne = 'clear'
    os.system(commandOne)

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
            if wordS[0:5] == "play ":
                    mkj.shortimportant("PLAY WORKING")
                    worder = str(wordS[6:40])
                    youtubeMusic = str("https://www.youtube.com/results?search_query=" + worder)
                    browser.get(youtubeMusic)
                    lucky = browser.find_element_by_css_selector("ytd-video-renderer.style-scope:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1) > yt-img-shadow:nth-child(1) > img:nth-child(1)")
                    lucky.click()
                    # oldVnew = browser.find_element_by_css_selector("#watch-card-title")
                    # print(oldVnew)
                    # if oldVnew:
                    #     lucky = browser.find_element_by_css_selector("ytd-video-renderer.style-scope:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1) > yt-img-shadow:nth-child(1) > img:nth-child(1)")
                    #     lucky.click()
                    # else:
                    #     lucky = browser.find_element_by_css_selector("#item-section-613394 > li:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > img:nth-child(1)")
                    #     lucky.click()
                    
            # PAUSE
            elif wordS[0:5] == "start" or wordS[0:4] == "play":
                mkj.shortimportant("PAUSE WORKING")
                pause = browser.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
                pause.click()

            # NEXT
            elif wordS[0:4] == "stop":
                mkj.shortimportant("STOP WORKING")
                pause = browser.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
                pause.click()

            # ADD
            elif wordS[0:3] == "add":
                songOne = [str(wordS[6:40]), "", ""]
                print(songOne[0])
                print(songOne[1])
                print(songOne[2])
                # songTwo = "https://www.facebook.com"
                # songThree = "https://www.google.com"
                # playlist = songOne + ", " + songTwo + ", " + songThree
                # player = playlist.split(", ")
                # print(player) #################### PRINT THE ARRAY
                # print(len(player)) ################# PRINT THE LENGTH

                i = 0
                for songs in songOne:
                    ytSmall = songOne[i]
                    ytMusic = "https://www.youtube.com/results?search_query=" + ytSmall
                    browser.get(ytMusic)
                    try:
                        adD = browser.find_element_by_css_selector("ytd-video-renderer.style-scope:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1) > yt-img-shadow:nth-child(1) > img:nth-child(1)")
                    except:
                        adD = browser.find_element_by_css_selector("ytd-video-renderer.style-scope:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1) > yt-img-shadow:nth-child(1) > img:nth-child(1)")
                    adD.click()
                    timeOfVideo = browser.find_element_by_class_name("ytp-chrome-controls") ## Not Working?
                    print(timeOfVideo)
                    time.sleep(1)
                    
                    i += 1

                # i = 0
                # for songs in songOne:
                    # i += 1
                # song = [x+1 for x in player]
                # for songs in player:
                #     browser.get(player[0])
                # mkj.shortimportant("ADD WORKING")
                # youtubeMusic = str("https://www.youtube.com/results?search_query=" + songOne)
                # print(youtubeMusic)
                # browser.get(youtubeMusic)

            # SEARCH
            elif wordS[0:6] == "search": 
                mkj.shortimportant("SEARCH WORKING")
                worder = str(wordS[6:40])
                youtubeMusic = str("https://www.youtube.com/results?search_query=" + worder)
                browser.get(youtubeMusic)