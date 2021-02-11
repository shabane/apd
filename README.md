# apd
### aparat downloader is a program that make downloading video's and playlist easy from aparat.
apd is the main of the program which conrtrol all the module and maintain the cli interface.
  
all you need for download one video is thet paste video page link after the command apd. like:
```apd https://aparat.com/some/videohash```
![Download One Vdeo](/image/download_one_video.gif)

or if you need to download whole video of a playlist put --playlist before or after the link that have 
a playlist. like this:
``` apd https://aparat.com/some/videohash --playlist ```
![Download all playlist](/image/download_all_playlist.gif)

if you use --list option, it will print the url/url's to stdout and then you can redirect them to a file.
``` apd https://aparat.com/some/videohash --playlist --list ```
![get video download url](/image/list_one_video.gif)
Or
![get playlist video download url](/image/list_all_playlist.gif)



and the last option is --quality this option get a number and try to find the video download url with that quality.
```apd https://aparat.com/some/videohash --playlist --list --quality 1080```

## all the option has a short way to use:

	> quality	| -q
		
	> playlis	| -p
		
	> list		| -l
  
>note that if you use --list, apd won't download any video.

>note that if you don't specify quality, apd will try to find 480 quality.

# how to install on linux
1. first download this file [apd.tar](https://gateway.pinata.cloud/ipfs/QmWV2jprP66Y1JbLtXLXWq5LYeZa6VQZn3ayTNhaCqmQnv)
2. than extract it with ```tar -xf apd.tar``` command
3. enter ```chmod u+x ./install.sh```
4. run ```./install.sh```
5. yo made it, now you can run ```apd``` command.
6. ```apd "aparat link" [option]```

# how to install on windows
1. first download the windows version of apd from this link [apt.tar](https://gateway.pinata.cloud/ipfs/QmX3iLPWKWBC2o3xJBFqruoDdegdCbLRMdkXBtSao9WSRP)
2. extract the file
3. open CMD and go to the apd dircectory
4. enter ```apd.py "apart link" [option]```
