from __future__ import unicode_literals
#selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#youtube-dl and supporters imports
import os
os.system("pip install --upgrade youtube-dl") #this will install youtube dl if it isn't already
import youtube_dl
from os import startfile
#configure the webdriver
chrome_options = Options() 
chrome_options.add_argument("--headless") #this will make the browser headless
serviceObject = Service("chromedriver.exe") #this will make the service object
driver = webdriver.Chrome(service=serviceObject, options=chrome_options) 
#configure youtube-dl
#used to grab the filename 
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
ydl_opts = {
    'format': 'mp4',
    'quiet': True,
    'outtmpl': 'output.mp4'
}
_first = True #this is a flag to check if it's the first time the menu is being displayed

def main(): 
    global _first
    if _first:
        print("Youtube CLI - Distraction Free Youtube\nType help for a list of commands")
        _first = False
    menuinput = input("Enter a command:")
    try:
        menu_switch(menuinput)
    except ValueError:
        main()
    
#get the driver to search for a query and return a list of the videos
def search():
    query = input("Enter a search query: ")
    driver.get("https://www.youtube.com/results?search_query=" + query)
    titles = driver.find_elements(By.XPATH, '//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
    titles_list = []
    for p in range(len(titles)):
        titles_list.append(titles[p].text)
    #print like a million blank lines so the dumb shit error goes away
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(*titles_list, sep = "\n")
    main()
#given a youtube link play it, this should just invoke youtube-dl and then open the file once it's downloaded
def playlink():
    #stub
    return
def playtitle():
    print("Enter the title of the video that you'd like to play")
    title = input()
    return
#pseudo switch case statement that handles menu inputs
def menu_switch(menuinput):
    if menuinput == "help":
        print("help - displays this menu:\nsearch - displays search results for a query\nplaylink - plays a video from a link\nplaytitle - plays a given it's title\nexit - exits the program")
        main() #because this doesn't invoke a helper function, we need to manually return to main
    elif menuinput == "search":
        search()
    elif menuinput == "playlink":
        playlink()
    elif menuinput == "playtitle":
        playtitle()
    elif menuinput == "exit":
        quit()
    else:
        print("No such command, type help for a list of commands")
        raise ValueError("Invalid input")
def playvideo(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=1FcR1PDzC94'])
    startfile("output.mp4")
    input("press enter when you're done watching the video")
    os.remove("output.mp4")
    

        
    
    
#testing playvideo
playvideo("https://youtu.be/K_CaG_-h5Ho")       
#main()
    
        
    
    
    





