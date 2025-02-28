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
#configure the webdriver
ffox_options = Options() 
ffox_options.add_argument("--headless") #this will make the browser headless (runs invisibly)
ffox_options.add_argument("--log-level=3") #log level 3 supresses all output to the console
serviceObject = Service("geckodriver.exe") #required selenium thing
driver = webdriver.Chrome(service=serviceObject, options=ffox_options) 
#generic imports
import time
import audioread
#psutil is used to auto-close the player process
import psutil

#configure youtube-dl
ydl_opts_video = {
    'format': 'mp4/bestaudio/best',
    'silent': True,
    'sponsorblock': 'remove-sponsor/all',
    'cookies-from-browser': 'firefox'
}
ydl_opts_audio = {
    'format': 'm4a/bestaudio/best',
    'quiet' : True,
    'sponsorblock': 'remove-sponsor/all'
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
    #wait for the page to load
    titles_list = []
    href_list = []
    #if we don't wait for the page to load, we'll get an empty list, so repeat the scrape process until we get some results
    while (len(titles_list) == 0):
        time.sleep(0.5)
        #titles = driver.find_elements(By.XPATH, '//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
        titles = (driver.find_elements(By.ID, 'video-title')) #this appears to work better than xpath, 
        #get the title and href of each video
        for p in range(len(titles)):
            titles_list.append(titles[p].get_attribute("title"))
            href_list.append(titles[p].get_attribute("href"))
    #because youtube sometimes serves video-title objects that are empty, we need to filter them out
    for i, t in enumerate(titles_list):
        if t == '':
            titles_list.pop(i)
            href_list.pop(i)
    #print the filtered list of videos
    print("WARNING: Videos empty URL's will cause an error!")
    for i in range(len(titles_list)):
        print(f"{str(i+1)} : {titles_list[i]} :: {href_list[i]}")
    print("Enter a number to play the video, otherwise make any input to exit")
    vid_select = input()
    try:
        vid_select_int = int(vid_select)
    except:
        TypeError
        main()
    playvideo(href_list[vid_select_int-1])
    main()
#this works basically the same as before but using a different player settings
def music():
    query = input("Enter a search query: ")
    driver.get("https://www.youtube.com/results?search_query=" + query)
    #wait for the page to load
    titles_list = []
    href_list = []
    #if we don't wait for the page to load, we'll get an empty list, so repeat the scrape process until we get some results
    while (len(titles_list) == 0):
        time.sleep(0.5)
        #titles = driver.find_elements(By.XPATH, '//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
        titles = (driver.find_elements(By.ID, 'video-title')) #this appears to work better than xpath, 
        #get the title and href of each video
        for p in range(len(titles)):
            titles_list.append(titles[p].get_attribute("title"))
            href_list.append(titles[p].get_attribute("href"))
    #because youtube sometimes serves video-title objects that are empty, we need to filter them out
    for i, t in enumerate(titles_list):
        if t == '':
            titles_list.pop(i)
            href_list.pop(i)
    #play the first result that comes up from the query
    try:
        playaudio(href_list[0])
    except IndexError:
        print("No results found")
        main()
    main()
    

#pseudo switch case statement that handles menu inputs
def menu_switch(menuinput):
    if menuinput == "help":
        print("help - displays this menu:\nsearch - displays search results for a query\nmusic - plays a song by title\nexit - exits the program")
        main() #because this doesn't invoke a helper function, we need to manually return to main
    elif menuinput == "search":
        search()
    elif menuinput == "music":
        music()
    elif menuinput == "playlib":
        playlibrary()
    elif menuinput == "exit":
        quit()
    else:
        print("No such command, type help for a list of commands")
        raise ValueError("Invalid input")
def playlibrary():
    #get a list of all the files in the music_library folder
    library = os.listdir("music_library")
    #print the list of files
    for i in range(len(library)):
        print(str(i+1)+". "+library[i])
    #ask the user to select a file
    print("Enter a number to play a specific file, \nEnter 0 to play them all \nOtherwise make any input to exit")
    file_select = input()
    try:
        file_select_int = int(file_select)
    except:
        TypeError
        main()
    #play the file
    if (file_select_int == 0):
        for i in range(len(library)):
            startfile("music_library\\"+library[i])
            #find the length of the file and wait that long
            with audioread.audio_open("music_library\\"+library[i]) as f:
                length = f.duration
                time.sleep(length)
    else:
        try:
            startfile("music_library\\"+library[file_select_int-1])
        except FileNotFoundError:
            print("File not found, exiting to main menu")
    main()
#given a youtube link, download the video and play it
def playvideo(link):
    URLS = [link]
    with YoutubeDL() as ydl:
        ydl.download(URLS)
        #return the relative path of the file
    for file in os.listdir("."):
        if file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".mkv"):
            outfile = file
    startfile(outfile)
    input("press enter when you're done watching the video (player must be closed)")
    [print(proc.info) for proc in psutil.process_iter(['pid', 'name'])]
    for proc in psutil.process_iter(['pid', 'name']):    
        #strip .exe from the name to be platorm agnostic
        proc.info['name'] = proc.info['name'].replace('.exe', '')
        if proc.info['name'] in ['vlc', 'wmplayer', 'mplayer', 'mpv', 'iTunes', 'QuickTimePlayer']:
            proc.terminate()
            proc.wait()
    #close the player window 
    os.remove(outfile)
    main()  


#this is the same as playvideo but with different settings
def playaudio(link):
    URLS = [link]
    with YoutubeDL(ydl_opts_audio) as ydl:
        ydl.download(URLS)
        #return the relative path of the file
        outfile = ydl.prepare_filename(ydl.extract_info(URLS[0], download=False))
    os.rename(outfile, "music_library\\"+outfile)
    startfile("music_library\\"+outfile)
    
#main loop    
main()
        
    
    
    





