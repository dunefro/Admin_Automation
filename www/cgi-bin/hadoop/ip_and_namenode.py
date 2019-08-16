#!/usr/bin/python36

import subprocess as sp
import cgi
import cgitb
cgitb.enable()

print("content-type: text/html")
print()

print("<form action='http://192.168.43.125/cgi-bin/hadoop/namenode.py' >")
print("Enter the IP: <input name='ip' /><br>")
print("Enter the password <input type=password name='pass' ><br>")
print("<input type='submit' value='Setup' />")
print("</form>")
