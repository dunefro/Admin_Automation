import docker

client = docker.from_env()

def send_mail(mail=None, dunefro=None):
    client.containers.run(image='dunefro/mail')