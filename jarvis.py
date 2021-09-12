
import speech_recognition as sr
import wikipedia
import pyttsx3
import pyaudio
import datetime
import os
import webbrowser
from selenium import webdriver 
import ctypes
import pyautogui
import json5,requests,time
#import pywhatkit for send whatsapp msg using python
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import QTimer,QDate,QTime,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_jarvisUI   
import sys 


#import an engine for speech
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

#voice speed
rate=engine.getProperty('rate')
engine.setProperty('rate',200)


#web driver for browsing
'''
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()
'''

#for speech, pass text in this module 
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wish me function
def welcome():
    hour=int((datetime.datetime.now()).hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    if hour>=12 and hour<17:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("i'm your jarvis assistant")

#voice to text


#wiki
def wikipedia_search():
    speak("searching details....Wait")
    task.replace("wikipedia","")
    results=wikipedia.summary(task,sentences=2)
    print(results)
    speak(results)

#device lock
def lock_device():
    speak("locking the device")
    ctypes.windll.user32.LockWorkStation()

#explore file in system
def fileExplorer():
    speak("why not...which disk do you want to open")
    disk=takeTask().lower()
    if "open f" in disk:
        os.startfile("F:")
    elif "open g" in disk or "open ji" in disk:
        os.startfile("G:")

#top news
def topNews():
    try:
        key=open("key.txt",'r').read()
    except:
        print("file not found")
        return
    
    url=f'https://newsapi.org/v2/everything?q=keyword&apiKey={key}'

    try:
        response=requests.get(url)
    except:
        speak("can't get your request. check your network connection")
        return
    
    news=json5.loads(response.text)
    speak("how many news want to listen")
    no_of_news=int(input())
    c=0
    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']), "\n\n")
        speak(str(new['title']))
        print('______________________________________________________\n')
  
        engine.runAndWait()
  
        print(str(new['description']), "\n\n")
        speak(str(new['description']))
        engine.runAndWait()
        print("..............................................................")
        time.sleep(2)
        c+=1

        if c==no_of_news:
            break



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()
    
    def takeTask(self):
        re=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            #re.pause_threshold=1
            audio=re.listen(source)  #,timeout=1,phrase_time_limit=5
            try:
                print("Recognising......")
                text=re.recognize_google(audio,language="en-us")        #for english text
                #text=re.recognize_google(audio,language="hi-In")       #for hindi text
                print(text)
            except Exception as e:
                print(e)
                speak("I am not getting anything sir...please say something")
                return "None"
            return text

    def TaskExecution(self):
        speak("Welcome back sir")
        welcome()
        while 1:
            self.task=self.takeTask().lower()         #lower for converting into lowercase        
            
            if "open google" in self.task:
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" #webbrowser.register('chrome',Chrome('chrome'))
                chrome_browser=webbrowser.get(chrome_path)
                speak("what do you want to search")
                search_query=self.takeTask()
                chrome_browser.open(f"https://google.com/search?q={search_query}")

            elif "play song" in self.task:
                speak("which song do you want to listen")
                search_query=self.takeTask()
                webbrowser.open(f"https://youtube.com/search?q={search_query}")
                #driver.get("http://www.youtube.com/results?search_query =" + '+'.join(search_query))

            
            elif "wikipedia" in self.task:
                wikipedia_search()

            elif 'lock window' in self.task:
                lock_device()
    
            elif "ok open a folder for me" in self.task:
                fileExplorer()
                    
            elif "what is today's temperature" in self.task:
                webbrowser.open()
            
            elif "today latest news" in self.task:
                topNews()

            elif "close" in self.task:
                speak("good bye sir. have a nice day")
                exit()



startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("G:\python\Jarvis\livegui.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("G:\python\Jarvis\initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString("hh:mm:ss")
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())
