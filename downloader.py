# this module will download all the video from the list
import requests
import sys
import json

headers = {}
with open(f"{sys.path[0]}/headers", "r") as fli:
        fli = json.load(fli)
        if type(fli) != dict:
            print("err: the header file should be a json file", file=sys.stderr)
        elif type(fli) == dict:
            headers = fli

def main(videos):
    for url,name in videos:
        print("Downloading", name)
        tmpfile = requests.get(url, headers=headers)
        if(tmpfile.status_code == 200):
            with open(name, "wb") as videofile:
                videofile.write(tmpfile.content)
        else:
            print("http status is:", tmpfile.status_code)
            sys.exit(tmpfile.status_code)
