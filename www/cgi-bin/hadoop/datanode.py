#!/usr/bin/python36

import subprocess as sp
import cgi
import cgitb
cgitb.enable()

print("content-type: text/html")
print()

data=cgi.FieldStorage()
ip=data.getvalue('ip')
mip=data.getvalue('mip')
sp.getoutput(f"sudo ssh root@{ip}rpm -ivh  /root/jdk-8u171-linux-x64.rpm")
sp.getoutput(f"sudo ssh root@{ip} export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64")
sp.getoutput(f"sudo ssh root@{ip} 'echo  JAVA_HOME=/usr/java/jdk1.8.0_171-amd64 >> /root/.bashrc' ")
sp.getoutput(f"sudo ssh root@{ip} 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH ' ")
sp.getoutput(f"sudo ssh root@{ip} 'echo  PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH >> /root/.bashrc' ")
sp.getoutput(f"sudo ssh root@{ip} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
f=open("hdfs-site.xml","w")
f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.data.dir</name>
<value>/data</value>
</property>

</configuration>
""")
f.close()
f=open("core-site.xml","w")
f.write(f"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{mip}:9001</value>
</property>

</configuration>
""")
f.close()
sp.getoutput(f"sudo scp /var/www/cgi-bin/hdfs-site.xml {ip}:/etc/hadoop/")
sp.getoutput(f"sudo scp /var/www/cgi-bin/core-site.xml {ip}:/etc/hadoop/")
sp.getoutput(f"sudo ssh root@{ip} hadoop-daemon.sh start datanode")
x=sp.getoutput("sudo ssh root@{ip} jps | grep DataNode")
if x=='':
  print("Unsuccessful")
else:
  print("Successful")

