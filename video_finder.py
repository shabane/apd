# this module will find one video with given quality

from bs4 import BeautifulSoup as bs
import requests
import sys
import re


def main(link, quality):
    if(link[0:4] == "http"):
        req = requests.get(link)
        result = req.content
        soup = bs(result, "html.parser")
        fquality = soup.find("div",attrs={"class":"dropdown-content"}).find_all("a")
        videolinks = re.findall("href=\"(.*)\".*target", str(fquality))
    else:
        print("Check the link")
        sys.exit(1)