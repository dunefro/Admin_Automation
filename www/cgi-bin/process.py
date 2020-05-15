from flask import Flask
import docker
from helpers.docker_helper import container_list
from helpers.db_helper import create_db
from helpers.mail_helper import send_mail
from helpers.paas_helper import create_python_shell
import logging

logging.basicConfig(level=logging.INFO)

app=Flask(__name__)

@app.route('/',methods=['GET'])
def main_route():
    return 'Up and Running !!!'


@app.route('/healthz',methods=['GET'])
def check_health():
    return {'status': 'success', 'response': 'Api is working fine'}

@app.route('/docker/healthz',methods=['GET'])
def check_docker_health():
    try:
        client = docker.from_env()
        client.info()
        return {'status': 'success', 'response': 'Docker is running in the cluster'}
    except:
        return {'status': 'Failure', 'response': 'Docker is not present'}

@app.route('/docker/table',methods=['GET'])
def check_docker_table():
    obj_list = container_list()
    response = 'NAME\t\t\t\t\t\tIMAGE\t\t\t\t\t\tID\t\t\t\t\t\tSTATUS\n'
    response_template = '{}\t\t\t\t\t\t{}\t\t\t\t\t\t{}\t\t\t\t\t\t{}\n'
    for obj in obj_list:
        response += response_template.format(obj.name,obj.image.tags,obj.short_id,obj.status)
    return response

@app.route('/database/<string:db>',methods=['GET'])
def db(db):
    return str(create_db(db))

@app.route('/mail/<string:name>',methods=['GET'])
def write_mail(name):
  return str(send_mail(name))

@app.route('/paas/python',methods=['GET'])
def paas_python():
    create_python_shell()
    return str(True)


if __name__=='__main__':
    app.run(port=5000)

# #!/usr/bin/python36
#
# print("content-type: text/html")
#
# import subprocess as sp
# import cgi
# import cgitb
# import webbrowser as wb
# cgitb.enable()
#
# data=cgi.FieldStorage()
#
# q=data.getvalue('q')
# if "status" in q and "docker" in q:
#   #print("location: http://172.20.10.2/cgi-bin/docker_start.py")
#    print("location: http://192.168.43.125/cgi-bin/docker/docker_table.py")
#    print()
#
# elif "paas" in q or "platform" in q:
#   print("location: http://192.168.43.125:3200/")
#   print()
#
# elif "container" in q:
#  # print()
#   print("location: http://192.168.43.125:2200")
#   print()
#
# elif "software" in q and "firefox" in q or "Firefox" in q:
#   sp.getoutput("docker start fire")
#   print("location: http://192.168.43.125:3333")
#   print()
#
# elif "software" in q and "notepad" in q or "Notepad" in q:
#   sp.getoutput("docker start gediting")
#   print("location: http://192.168.43.125:2233")
#   print()
#
# elif "ec2" in q:
#   print()
#   print(sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/aws/ec2.yml"))
#
# elif "storage" in q:
#   print()
#   print("storage")
#   x=sp.getoutput("ls / | grep shared")
#   if x=='':
#     print(sp.getoutput("sudo mkdir /shared"))
#     print(sp.getoutput("sudo chmod 777 /shared"))
#     print(sp.getoutput("sudo echo -e '/shared	*(rw,no_root_squash)' >> /etc/exports"))
#     y=sp.getoutput("sudo showmount -e | grep /shared")
#     if y=='':
#       print("Unsuccessful")
#     else:
#       print("Successful")
#   else:
#     print("Already giving the service")
# elif "s3" in q:
#   print()
#   print(sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/aws/s3.yml"))
# elif "hadoop" in q or "Hadoop" in q and "namenode" in q:
#   print("location: http://192.168.43.125/cgi-bin/hadoop/ip_and_namenode.py")
#   print()
# elif "hadoop" in q or "Hadoop" in q and "datanode" in q:
#   print("location: http://192.168.43.125/cgi-bin/hadoop/ip_and_datanode.py")
#   print()
# elif "mail" in q:
#   print()
# #  print(sp.getoutput('sudo ansible-playbook /var/www/cgi-bin/mail/mail.yml'))
#   if "failed=0" in sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/mail/mail.yml"):
#     print("Mail Successfully Sent ")
# else:
#   print()
