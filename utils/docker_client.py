import docker

def get_docker_client():
    """
    Create and return a Docker client using environment variables.

    Returns:
        docker.DockerClient: A client connected to the local Docker daemon.
    """
    return docker.from_env()
