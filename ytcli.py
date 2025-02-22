from __future__ import unicode_literals
#selenium imports
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
#youtube-dl and supporters imports
import os
#os.system("pip install -U -q -q -q yt-dlp") #this will install youtube dl if it isn't already
#os.system("pip install -U -q -q -q selenium") #the -q -q -q will supress any pip errors (path error)
#os.system("pip install -U -q -q -q audioread") 
from yt_dlp import YoutubeDL
from os import startfile
#generic imports
import time
import audioread

"""
We doing that object oriented shit now (sad)
"""
class ytScraper:
    def __init__(self):
        ffox_options = Options() 
        ffox_options.add_argument("--headless") #this will make the browser headless (runs invisibly)
        ffox_options.add_argument("--log-level=3") #log level 3 supresses all output to the console
        serviceObject = Service("geckodriver.exe") #required selenium thing
        self.driver = webdriver.Chrome(service=serviceObject, options=ffox_options)
        
        #configure youtube-dl
        self.ydl_opts_video = {
            'format': 'mp4/bestaudio/best',
            'silent': True,
            'sponsorblock': 'remove-sponsor/all'
        }       
        self.ydl_opts_audio = {
            'format': 'm4a/bestaudio/best',
            'quiet' : True,
            'sponsorblock': 'remove-sponsor/all'
        }
        
        print("Initialization Complete")
        print("Youtube CLI - Distraction Free Youtube\nType help for a list of commands")
        
    def run(self):
        command = input("Enter a command: ")
        if command == "search":
            self.search()
        elif command == "help":
            print("Youtube CLI - Distraction Free Youtube\nType help for a list of commands")
            
        
        
                