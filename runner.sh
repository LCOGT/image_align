#!/bin/bash

python main.py --out_dir /Users/egomez/Downloads/jupiter/ -r 641102 -n -f zs -s
ffmpeg -framerate 5 -pattern_type glob -i "/Users/egomez/Downloads/jupiter/*.jpg" -vcodec libx264  -pix_fmt yuv420p latest.mp4
