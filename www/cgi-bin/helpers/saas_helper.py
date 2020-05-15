import docker
from random import randint
from helpers.paas_helper import check_port
import logging

logging.basicConfig(level=logging.INFO)
client=docker.from_env()

def create_firefox():
    while True:
        paas_port = randint(49152, 65535)
        port_list = [port for port in range(49512, 65536) if check_port(port) == 0]
        if paas_port not in port_list:
            logging.info(paas_port)
            client.containers.run('dunefro/firefox:v1', detach=True, tty=True, ports={'3333/tcp': paas_port})
            break

    return paas_port