mogrify -format tiff -separate -channel Gray -compress RLE *.svg
mogrify -black-threshold 200 -white-threshold 200 -compress RLE *.tiff



