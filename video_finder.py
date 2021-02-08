# this module will find one video with given quality

from bs4 import BeautifulSoup as bs
import requests
import sys
import re

lstlink = []
tmpq = str()
def main(link, quality):
    tmpq = quality
    quality = ".*"+str(quality)+".*"    # This regex find the specify quality in the list of all quality
    if(link[0:23] == "https://www.aparat.com/"):
        req = requests.get(link)
        if(req.status_code == 200):
            result = req.content
            soup = bs(result, "html.parser")
            # Finding name of video
            name = soup.h1.string+".mp4"
            # Finding video download url
            fquality = soup.find("div",attrs={"class":"dropdown-content"}).find_all("a")
            videolinks = re.findall("href=\"(.*)\".*target", str(fquality)) # This Regex return a list of all quality of video
            for i in videolinks:
                if(re.findall(quality, i)):
                    return i, name
        else:
            print("http status code is: "+req.status_code)
    else:
        print("Check the link and try again")
        sys.exit(1)