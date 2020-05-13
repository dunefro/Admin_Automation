import docker
import logging

logging.basicConfig(level=logging.INFO)
client = docker.from_env()

def create_db(db_name):
    if db_name == 'redis':
        client.containers.run(image='redis:2.6-32bit')
    logging.info(db_name)
    return True