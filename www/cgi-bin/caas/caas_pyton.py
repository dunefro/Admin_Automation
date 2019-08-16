#!/usr/bin/python36

print("content-type: text/html")

import subprocess as sp
import cgi
import cgitb

cgitb.enable()

print("location: http://192.168.43.125:3200")
print()
