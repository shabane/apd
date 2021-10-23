# this module will find and list all video of playlist url with given quality
from bs4 import BeautifulSoup as bs
import requests
import re
import sys

videos = list()



# def find_from_inside(pllink):

#TODO this fucking shit does not work, may becasue the aparat change the fron, how ever this should change to a nother crowlwe

def main(link):
    if(link[0:32] == "https://www.aparat.com/playlist/"):
        req = requests.get(link)
        if(req.status_code == 200):
            soup = bs(req.content, "html.parser")
            soup = soup.find_all("a",attrs={"class":"light-80 dark-10"})
            soup = bs(str(soup), "html.parser")
            for i in soup.find_all("a", attrs={"class":"light-80 dark-10"}):
                videos.append('https://aparat.com'+i["href"])
            return videos
        else:
            print("err: http status code:", req.status_code)
            sys.exit(req.status_code)
    elif(link[0:23] == "https://www.aparat.com/"):
        link = "https://aparat.com/playlist/" + re.findall("\=(.*)", link)[0] # this regex return play list address
        print(link)
        req = requests.get(link)
        if(req.status_code == 200):
            soup = bs(req.content, "html.parser")
            soup = soup.find_all("a",attrs={"class":"light-80 dark-10"})
            soup = bs(str(soup), "html.parser")
            for i in soup.find_all("a", attrs={"class":"light-80 dark-10"}):
                videos.append('https://aparat.com'+i["href"])
            return videos
        else:
            print("err: http status code:", req.status_code)
            sys.exit(req.status_code)



if __name__ == '__main__':
    print('running')
    print(main('https://www.aparat.com/v/FKi9I?playlist=1284902'))