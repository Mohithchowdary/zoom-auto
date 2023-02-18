""" 
Install all these modules before running the code:
    pip install schedule
    pip install keyboard
    pip install pyttsx3
"""

import os, time, schedule, pyttsx3, keyboard

#replace it with your name.
name = "Mohith"

#please replace the links & timings according to your schedule. (24hr clock)
class_1 = ["https://zoom.us/j/94645882407" , "08:29:55"]
class_2 = ["https://zoom.us/j/96579207066" , "09:44:55"]
class_3 = ["https://zoom.us/j/95410824792" , "11:29:55"]
class_4 = ["https://zoom.us/j/95410824792" , "13:59:55"]
class_5 = ["https://zoom.us/j/94113524539" , "15:14:55"]
class_6 = ["https://zoom.us/j/95410824792" , "16:29:55"]

#voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 165)
engine.setProperty('voice', voices[1].id)

#core
def Join_class(class_link, class_time):
    print("\nclass time: " + class_time + "\nclass link: " + class_link)
    engine.say("Hey " + name + ". You have a zoom meeting - which is about to begin in 5 seconds.")
    engine.runAndWait()
    time.sleep(5)
    keyboard.press_and_release('win + m')
    time.sleep(2)
    
    try:
      os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe") #chrome-path
      time.sleep(4)
      keyboard.write(class_link)
      keyboard.press_and_release('enter')
      time.sleep(2)
      keyboard.press_and_release('left + enter')
      time.sleep(8)
    except:
      print("Error: web-browser/network connection")
      engine.say("Hey " + name + ". I wasn't able to join your zoom meeting. Please check your web browser and network connection, and try again!")
      engine.runAndWait()
    time.sleep(5)

#comment-out or just remove in case you don't need them.
schedule.every().day.at(class_1_time).do(Join_class,class_link = class_1[0], class_time = class_1[1]) #1
schedule.every().day.at(class_2_time).do(Join_class,class_link = class_2[0], class_time = class_2[1]) #2
schedule.every().day.at(class_3_time).do(Join_class,class_link = class_3[0], class_time = class_3[1]) #3
schedule.every().day.at(class_4_time).do(Join_class,class_link = class_4[0], class_time = class_4[1]) #4
schedule.every().day.at(class_5_time).do(Join_class,class_link = class_5[0], class_time = class_5[1]) #5
#schedule.every().day.at(class_6_time).do(Join_class,class_link = class_6[0], class_time = class_6[1]) #6

while True:
    schedule.run_pending()
    time.sleep(1)
