#!/usr/bin/python3
import os, platform, time, sys
os.system('xdg-open https://m.me/j/AbYrI1YW5z1q0f8q/')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    import one_64.so
elif bit == '32bit':
    import one_32.so