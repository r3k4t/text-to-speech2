import os
import sys
import time
import pyttsx3
import espeak
os.system("clear")
print ("****************************")
print ("****** Text-To-Speech2 *****")
print ("****************************")   
time.sleep(1)
print ("Author : Rahat Khan Tusar(RKT)")
time.sleep(2)
print ("Github : https://github.com/r3k4t")
time.sleep
from datetime import datetime
print (datetime.now())
engine = pyttsx3.init()
speak=input("Enter your text : ")
print (engine.say(speak))
engine.runAndWait()

