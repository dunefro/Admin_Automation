#!/usr/bin/python36

print("content-type: text/html")
#print()
import subprocess as sp
import cgi
import cgitb
cgitb.enable()

data=cgi.FieldStorage()
dock_id=data.getvalue('id')
sp.getoutput(f"sudo docker stop {dock_id}")
#print(f"{dock_id}")
print("location: http://192.168.43.125/cgi-bin/docker_table.py")
print()
