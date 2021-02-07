#!/bin/python3
import nd
import pld
import argparse

# Description's
play_list_des = "If video have play list find and download all playlist. if play list url given, download all play list"
q_des = "144, 360, 480, 720, 1080"
spider_des = "If --spider or -s specify, it will crawl the page given and download all the play list"
just_list_des = "Just print the video's link in stdout"

# Craate Commad line Option 
parser = argparse.ArgumentParser(description = "Any Aparat downloader such as Playlist Or Normal video")
parser.add_argument("link", help="Page link")
parser.add_argument("--quality", "-q", help=q_des, default="480")
parser.add_argument("--find-playlist", "-p", help = play_list_des)
parser.add_argument("--spider", "-s", help = spider_des)
parser.add_argument("--just-list", "-l", help = just_list_des)

args = parser.parse_args()
link = args.link
quality = args.quality
spider = args.spider
just_link = args.justlist
