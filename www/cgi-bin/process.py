from flask import Flask , Response
import docker
from helpers.docker_helper import container_list
from helpers.db_helper import create_db
from helpers.mail_helper import send_mail
from helpers.paas_helper import create_python_shell
from helpers.saas_helper import create_firefox , create_notepad
import time
import cv2
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
    return str(create_python_shell())

@app.route('/saas/firefox',methods=['GET'])
def saas_firefox():
    return str(create_firefox())

@app.route('/saas/notepad',methods=['GET'])
def saas_notepad():
    return str(create_notepad())

@app.route('/cam/',methods=['GET'])
def camera_stream():
    # camera_req = request.json
    # while True:
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    video_stream = cv2.VideoCapture('rtsp://live1.brownrice.com:1935/westland/westland.stream')
    while True:
        success, frame_stream = video_stream.read()
        ret, buffer = cv2.imencode('.jpg', frame_stream)
        time.sleep(0.05)
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n\r\n')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)

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
