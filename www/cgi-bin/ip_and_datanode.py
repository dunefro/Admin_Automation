#!/usr/bin/python36

import subprocess as sp
import cgi
import cgitb
cgitb.enable()

print("content-type: text/html")
print()

print("<form action='http://172.20.10.2/cgi-bin/namenode.py' >")
print("Enter the IP: <input name='ip' /><br>")
print("Enter the master IP: <input name='mip' /><br>")
print("Enter the password <input type=password name='pass' ><br>")
print("<input type='submit' value='Setup' />")
print("</form>")
