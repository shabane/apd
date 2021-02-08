#!/bin/python3
# The main of program include cli interface

import downloader as dl
import video_finder as vf
import play_list_finder as plf
import argparse

# Description for each option and paramer
play_list_des = "If video have play list, find and download all playlist. if play list url given, download all play list. -l will print all the links on stdout\n"
q_des = "144, 360, 480, 720, 1080"
spider_des = "If --spider or -s specify, it will crawl the page given and download all the play list. -l will print all the links on stdout"
just_list_des = "Just print the video's link in stdout"
primary_des = "Any Aparat link such as Playlist Or Normal video"

# Craate Commad line interface
parser = argparse.ArgumentParser(prog="apd", description=primary_des)
parser.add_argument("link", help="Page link")
parser.add_argument("-q", "--quality", help=q_des, default="480", type=int)
# Optional option's
parser.add_argument("-p", "--playlist", help=play_list_des, action="store_true")
parser.add_argument("-s", "--spider", help=spider_des, action="store_true")
parser.add_argument("-l", "--just-list", help=just_list_des, action="store_true")

# Set the variable
args = parser.parse_args()
link = args.link
quality = args.quality
playlist = args.playlist
spider = args.spider    
just_list = args.just_list

videos = [] # Video's will list the video url and it's name on a tuple

if(link != None):
    if(playlist == True):
        pass
    else:
        videos.append(vf.main(link, quality))
    if(spider == True):
        pass
    if(just_list == True):
        pass
else:
    print("Did you miss link ?")

print(videos)