import docker
import logging

logging.basicConfig(level=logging.INFO)
client = docker.from_env()

def create_db(db_name):
    logging.info(db_name)
    return True