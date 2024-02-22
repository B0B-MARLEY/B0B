#!/data/data/com.termux/files/usr/bin/python
import platform,os,sys
bit = platform.architecture()[0]
if bit == '64bit':
    import file64
elif bit == '32bit':
    import file32
 
