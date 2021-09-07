# This Python file uses the following encoding: utf-8
#-*- coding: utf-8 -*-

# https://github.com/jiaaro/pydub
# Dependencies: ffmpeg or libav
#               http://www.ffmpeg.org/
#               https://libav.org/
#               ffmpeg.exe
#               ffprobe.exe

import os
from glob import glob
from pydub import AudioSegment
from pydub.utils import mediainfo

file_path = './result/'
if (not os.path.isdir(file_path)):
    os.mkdir(file_path)

for file_name in glob('./*.wav'):
    original_bitrate = mediainfo(file_name)['bit_rate']
    audio = AudioSegment.from_file(file_name)

    new_file_name = file_path + file_name.replace('.wav', '.pcm')
    print(file_name, '--->', new_file_name)
    audio.export(new_file_name, format = 's16le', bitrate = original_bitrate)
