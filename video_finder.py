# this module will find one video with given quality

from bs4 import BeautifulSoup as bs
import requests
import sys
import re


def main(link, quality):
    found_or_not = str()
    quality = ".*"+str(quality)+".*"    # This regex find the specify quality in the list of all quality
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
                found_or_not = i
                return i, name
        if(len(found_or_not) <= 0):
            print("Video with given quality not found")
            sys.exit(20)
    else:
        print("err: http status code is: "+req.status_code)
        sys.exit(req.status_code)