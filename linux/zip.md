# zip & unzip

## zip
### unzip
```
unzip file to a new floder
unzip [file_name] -d [dir]
```

### zip
```
zip archivename.zip filename1 filename2 filename3

zip archivename.zip object_dir/*
# zip all the files under object_dir to archivename.zip
```



## tar
### unzip
```
tar -xzvf archivename.zip

x – instructs tar to extract the files from the zipped file
v – means verbose, or to list out the files it’s extracting
z – instructs tar to decompress the files – without this, you’d have a folder full of compressed files
f – tells tar the filename you want it to work on
To list the contents of a .tar file before you extract it, enter:

tar –tzf documents.tar.gz

To instruct tar to put the extracted unzipped files into a specific directory, enter:
tar –xvzf documents.tar.gz –C /home/user/destination
```


