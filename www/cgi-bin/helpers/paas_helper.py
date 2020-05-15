import  docker
import socket
from random import randint
import logging

logging.basicConfig(level=logging.INFO)
client = docker.from_env()

def _check_port(port_no):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex(('127.0.0.1', port_no))
    sock.close()
    return res

def create_python_shell():
    while True:
        paas_port = randint(49152,65535)
        port_list = [port for port in range(49512,65536) if _check_port(port) == 0 ]
        if paas_port not in port_list:
            logging.info(paas_port)
            client.containers.run('dunefro/pass_shell:v1', detach=True,tty=True,ports={'4200/tcp': paas_port})
            break
