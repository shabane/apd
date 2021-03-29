# apd
### aparat downloader is a program that make downloading video's and playlist easy from aparat.
apd is the main of the program which conrtrol all the module and maintain the cli interface.
  
all you need for download one video is to paste the video page link after the command apd. like:
```apd https://aparat.com/some/videohash```
![Download One Vdeo](/image/download_one_video.gif)

or if you need to download the whole videos of a playlist, put --playlist before or after the link of the playlist. Like this:
``` apd https://aparat.com/some/videohash --playlist ```
![Download all playlist](/image/download_all_playlist.gif)

if you use --list option, it will print the url/url's to stdout and then you can redirect them to a file.
``` apd https://aparat.com/some/videohash --playlist --list ```
![get video download url](/image/list_one_video.gif)
Or
![get playlist video download url](/image/list_all_playlist.gif)



To specify the quality, use --quality option and set your required quality. Like This:
```apd https://aparat.com/some/videohash --playlist --list --quality 1080```



if you need to download a specify scop of a playlist you should use --start and/or --end.
the --start specify that from which video should start the process.
and --end indicate that which video is the last video that should be process.
``` apd https://aparat.com/some/videohash --playlist --start 3 --end 13```

## some of the option has a short way to use:

> quality	| -q
		
> playlis	| -p
		
> list		| -l



>note that if you use --list, apd won't download any video.

>note that if you don't specify quality, apd will try to find 480 quality.

>note: you can use --start or --end singly, like:
``` apd https://aparat.com/some/videohash --playlist --start 5```

>note the default ending is the last video of playlist

>note: default begining is the first video of playlist


# how to install on linux
1. first download this file [apd](https://drive.google.com/drive/folders/1sQB0Akgg5ShKrI7GfVax_GniHoNQEhmm?usp=sharing)
2. than extract it with ```unzip apd.zip``` command
3. enter ```bash install.sh```
4. you made it, now you can run ```apd``` command.
5. ```apd "aparat link" [option]```

# how to install on windows
1. first download the windows version of apd from this link [apt](https://drive.google.com/drive/folders/1zktNueaedc1j5FJBT1Saa-uFSJbSPmFj?usp=sharing)
2. extract zip file
3. open CMD and go to the apd dircectory
4. enter ```apd.py "apart link" [option]```


### exit code is:
	0: every thing is great
	2: missing some option
	10: error in the apd
	20: error in video_finder
	30: error in play_list_finder
	40: error in downloader
	other error: all other error come from http status
