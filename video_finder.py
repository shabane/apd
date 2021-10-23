# this module will find one video with given quality

from bs4 import BeautifulSoup as bs
import requests
import sys
import re
import json

headers = {}
with open("headers", "r") as fli:
        fli = json.load(fli)
        if type(fli) != dict:
            print("err: the header file should be a json file", file=sys.stderr)
        elif type(fli) == dict:
            headers = fli

def main(link, quality):
    found_or_not = str()
    quality = ".*"+str(quality)+".*"    # This regex find the specify quality in the list of all quality
    req = requests.get(link, headers=headers)
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
            print(f"Video with given quality {quality} not found. link: {link}")
    else:
        print(link)
        print("err in video finder: http status code is: "+str(req.status_code))
        sys.exit(req.status_code)
