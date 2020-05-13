import docker

client = docker.from_env()

def send_mail():
    client.containers.run(image=dunefro/mail)