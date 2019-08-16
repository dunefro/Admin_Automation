#!/usr/bin/python36

print("content-type: text/html")
#print()

import subprocess as sp
import cgi
import cgitb
cgitb.enable()

data=cgi.FieldStorage()
dock_id=data.getvalue('id')

#print(sp.getoutput("sudo id"))
#print(f"{dock_id}")

sp.getoutput(f"sudo docker start {dock_id}")

print("location: http://192.168.43.125/cgi-bin/docker_table.py")
print()
