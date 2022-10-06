import sys
from dive import *
import os
print(os.path.join(os.path.expanduser('~'),'python','kaaviya.py'))
import glob
print(glob.glob('*main*.py'))
metadata = os.stat('main.py')
print(metadata.st_size)
print(approximate_size(metadata.st_size, False))
import time 
print(time.localtime(metadata.st_mtime))
# print(time.struct_time(tm_year, tm_mon, tm_mday, tm_hour,
#   tm_min, tm_sec, tm_wday, tm_yday, tm_isdst))
print(os.path.realpath('hello.py'))
