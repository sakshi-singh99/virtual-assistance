import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voices',voices[1].id)


#TO CONVERT TEXT TO SPPECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
#TO CONVERT SPEECH TO TEXT
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")
        except Exception as e:
            speak("say that again, please....")
            return "none"
        return query
#TO WISH
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Prisa, tell me how can i help you...")  

#SEND EMAIL
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("nishasakshi999@gmail.com","Pratiksha@99")
    server.sendmail('nishasakshi999@gmail.com',to,content)
    server.close()     


    #FOR TASK EXECUTION        
if __name__== "__main__":
        #speak("hello")
        #takecommand()
        wish()
        while True:
        #if 1:
            query = takecommand().lower()

            #LOGIC BUILDING FOR TASK
            #TO OPEN NOTEPAD
            if "open notepad" in query:
                npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories" 
                os.startfile(npath)

            #TO OPEN cmd
            elif "open command prompt" in query:
                os.system("start cmd")

            #OPEN CAMERA
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow("WebCam",img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindow() 

            #OPEN MUSIC
            elif "play music" in query:
                music_dir = "F:\\songs"
                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))

            #FOR IP ADDRESS
            elif  "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
                
            #SEARCH ON WIKIPEDIA
            elif "wikipedia" in query:
                speak("searching wikipedia....")
                query=query.replace("wikipedia","")
                result= wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                speak(result)

            #OPEN YOUTUBE    
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            #OPEN INSTAGRAM
            elif "open instagram" in query:
                webbrowser.open("www.instagram.com")

            #OPEN GOOGLE
            elif "open google" in query:
                speak("SAKSHI what should i search on google")
                cm=takecommand()
                webbrowser.open(f"{cm}")
                webbrowser.open("www.google.com")

            #OPEN WHATSAPP
            elif "send message on whatsapp" in query:
                kit.sendwhatmsg("+918789638725","Hii",20,31)

            #PLAY SONG ON YOUTUBE
            elif "play song on youtube" in query:
                kit.playonyt("intenstion")

            #SEND EMAIL
            elif "email to sakshi" in query:
                try:
                    speak("what should i say?")
                    content=takecommand()
                    to="nishasakshi999@gamil.com"
                    sendEmail(to,content)
                    speak("email has been send to sakshi")

                except Exception as e:
                    print(e)
                    speak("sorry,i am not able to send this email to sakshi")

            #PRAISE 
            elif "How are you" in query:
                speak("I am fine,how are you mam")        

            #NO WORK
            elif "no thanks" in query:
                speak("Thanks for using me,Have a good day")
                sys.exit()

            #ASK FOR OTHER TASK
            speak("hey SAKSHI,do you have any other work")
                