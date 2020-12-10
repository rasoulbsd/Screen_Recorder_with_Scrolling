@echo off
ffmpeg -f gdigrab -show_region 1 -framerate 40 -video_size 960x1000 -offset_x 0 -offset_y 0 -i desktop -t 00:00:15 out2.mp4 