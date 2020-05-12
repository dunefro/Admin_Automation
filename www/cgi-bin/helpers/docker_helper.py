import docker

client = docker.from_env()

def container_list():
    return client.containers.list(all=True)

if __name__=='__main__':
    # print(client.info())
    print(container_list())