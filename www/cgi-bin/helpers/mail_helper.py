import docker
import logging

logging.basicConfig(level=logging.INFO)

client = docker.from_env()

def send_mail(client_name):
    logging.info('Client mail request received {}'.format(client_name))
    if client_name == "one":
        client.containers.run(image='dunefro/mail:v3',environment=["MAIL=pareekvedant99@gmail.com"],detach=True)
        logging.info("Mail sent check the container logs or your inbox")
    # Space for adding more clients