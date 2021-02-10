# this module will find and list all video of playlist url with given quality
from bs4 import BeautifulSoup as bs
import requests
import re
import sys

videos = list()



# def find_from_inside(pllink):


def main(link):
    if(link[0:32] == "https://www.aparat.com/playlist/"):
        req = requests.get(link)
        if(req.status_code == 200):
            soup = bs(req.content, "html.parser")
            soup = soup.find_all("a",attrs={"class":"light-80 dark-10"})
            soup = bs(str(soup), "html.parser")
            for i in soup.find_all("a", attrs={"class":"light-80 dark-10"}):
                x = re.findall("this\.href\=\'(.*)\'", str(i))  # this regex return each page link
                videos.append("https://aparat.com"+x[0])
            return videos
        else:
            print("err: http status code:", req.status_code)
            sys.exit(req.status_code)
    elif(link[0:23] == "https://www.aparat.com/"):
        link ="https://aparat.com/playlist/"+re.findall("\=(.*)", link)[0] # this regex return play list address
        req = requests.get(link)
        if(req.status_code == 200):
            soup = bs(req.content, "html.parser")
            soup = soup.find_all("a",attrs={"class":"light-80 dark-10"})
            soup = bs(str(soup), "html.parser")
            for i in soup.find_all("a", attrs={"class":"light-80 dark-10"}):
                x = re.findall("this\.href\=\'(.*)\'", str(i))  # this regex return each page link
                videos.append("https://aparat.com"+x[0])
            return videos
        else:
            print("err: http status code:", req.status_code)
            sys.exit(req.status_code)