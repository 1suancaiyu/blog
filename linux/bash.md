## unzip
unzip archive to dir and rename the dir as same as archive
```
mkdir tmp
for f in *.zip; do unzip "$f" -d tmp && mkdir "${f%.zip}" && mv tmp/* "${f%.zip}"; done
rmdir tmp
```
