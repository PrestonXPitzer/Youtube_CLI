from __future__ import unicode_literals
#selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#youtube-dl and supporters imports
import os
os.system("pip install -U yt-dlp") #this will install youtube dl if it isn't already
from yt_dlp import YoutubeDL
from os import startfile
#configure the webdriver
chrome_options = Options() 
chrome_options.add_argument("--headless") #this will make the browser headless
serviceObject = Service("chromedriver.exe") #this will make the service object
driver = webdriver.Chrome(service=serviceObject, options=chrome_options) 
#configure youtube-dl
ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
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
    href_list = []
    for p in range(len(titles)):
        titles_list.append(titles[p].text)
        href_list.append(titles[p].get_attribute("href"))
        
    #print like a million blank lines so the dumb shit error goes away
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in range(len(titles_list)):
        print(str(i+1)+". "+titles_list[i])
    print("Enter a number to play the video, otherwise make any input to exit")
    vid_select = input()
    try:
        vid_select_int = int(vid_select)
    except:
        TypeError
        main()
    playvideo(href_list[vid_select_int-1])
    
    
        
    
        
        
    
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
    URLS = [link]
    with YoutubeDL() as ydl:
        ydl.download(URLS)
        #return the relative path of the file
        outfile = ydl.prepare_filename(ydl.extract_info(URLS[0], download=False))
        #remove the .webm extension and replace it with .mp4
        outfile = outfile[:-5] + ".mp4"
        print(outfile)
    startfile(outfile)
    input("press enter when you're done watching the video")
    os.remove(outfile)   
#main loop    
main()

    
        
    
    
    





