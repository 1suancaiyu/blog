mkdir tmp
for f in *.zip; do unzip "$f" -d tmp && mkdir "${f%.zip}" && mv tmp/* "${f%.zip}"; done
rmdir tmp
