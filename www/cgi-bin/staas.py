#!/usr/bin/python36

import subprocess as sp
import cgi
import cgitb

print(sp.getoutput("sudo id"))
