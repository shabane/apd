# this module will download all the video from the list
import requests
import sys

def main(videos):
    for url,name in videos:
        print("Downloading", name)
        tmpfile = requests.get(url)
        if(tmpfile.status_code == 200):
            with open(name, "wb") as videofile:
                videofile.write(tmpfile.content)
        else:
            print("http status is:", tmpfile.status_code)
            sys.exit(tmpfile.status_code)
