
#check for a file called chromedriver.exe

if [ ! -f chromedriver.exe ]; then
    echo "chromedriver.exe not found, please download it from https://chromedriver.chromium.org/downloads"
fi
 

if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it from https://www.python.org/downloads/"
    exit
fi

if [ ! -f ffmpeg.exe ]; then
    echo "ffmpeg.exe not found, please download it from https://ffmpeg.org/download.html"
fi


#check the local directiory for a folder called music_library
# if it does not exist, create it

if [ ! -d music_library ]; then
    mkdir music_library
fi


#at this point we are probably chillin
python3 main.py