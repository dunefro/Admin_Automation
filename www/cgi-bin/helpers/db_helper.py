import docker
import logging

logging.basicConfig(level=logging.INFO)
client = docker.from_env()

def create_db(db_name):
    logging.info('Received databse {}'.format(db_name))
    if db_name == 'redis':
        client.containers.run(image='redis:latest',detach=True)
    elif db_name == 'es':
        client.containers.run(image='elasticsearch:latest', detach=True)
    elif db_name == 'mysql':
        client.containers.run(image='mysql:latest', detach=True,environment=["MYSQL_ALLOW_EMPTY_PASSWORD=True"])
    elif db_name == 'mongodb':
        client.containers.run(image='mongo:latest', detach=True)
    else:
        logging.info('Specify a valid database')
    logging.info(db_name)
    return True