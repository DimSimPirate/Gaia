#!/bin/bash

out_dir=../out
src_dir=$out_dir/frames
suffix=$1

if [ -z "$suffix" ] 
then
  src_dir=../out/frames
  out_file=../out/sensor_readings.mp4
else
  src_dir=../out/frames/$suffix
  out_file=../out/sensor_readings_$suffix.mp4
fi

ffmpeg -r 8 -f image2 -i $src_dir/frame_%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p $out_file
