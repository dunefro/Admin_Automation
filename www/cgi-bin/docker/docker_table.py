#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp
import cgi
import cgitb
cgitb.enable()

print("<h1> <center> Docker Table </center></h1>")
print("""
<table border='5' align='center' >
<tr> <th> Container ID </th>
<th> Container Name </th>
<th> Image Name </th>
<th> Status </th>
<th> Action </th>
</tr>
""")


x=sp.getoutput("sudo docker container ls -a")
y=x.split("\n")[1:]
for i in y:
  print("<tr>")
  #print("<td>a</td>")
  #print("<td>b</td>")
  print(f"<td>{i.split()[0]}</td>")
  print(f"<td>{i.split()[-1]}</td>")
  print(f"<td>{i.split()[1]}</td>")
  if "Exited" in i:
    print("<td>Stopped</td>")
    print(f"<td><a href='http://192.168.43.125/cgi-bin/docker_start.py?id={i.split()[0]}'> Start </a></td>")
  else:
    print("<td>Running</td>")
    print(f"<td><a href='http://192.168.43.125/cgi-bin/docker_stop.py?id={i.split()[0]}'> Stop </a></td>")
  print("</tr>")
print("</table>")



# If ever encountered with an error of operation not permitted -  it is due to buffer size
