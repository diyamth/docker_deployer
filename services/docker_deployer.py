import asyncssh
from typing import Optional, Dict
from services.validators import InputValidator

class DockerDeployer:
    def __init__(self, hostname: str, username: str, private_key_path: str):
        # SSH connection parameters
        self.hostname = os.getenv("SSH_HOSTNAME")
        self.username = os.getenv("SSH_USERNAME")
        self.private_key_path = os.getenv("PRIVATE_KEY_PATH")

        # SSH connection handle
        self.connection: Optional[asyncssh.SSHClientConnection] = None

    async def connect(self):
        """
        Establish an SSH connection if not already connected.
        """
        if self.connection is None:
            self.connection = await asyncssh.connect(
                self.hostname,
                username=self.username,
                client_keys=[self.private_key_path],
                known_hosts=None
            )

    async def disconnect(self):
        """
        Close the SSH connection cleanly.
        """
        if self.connection:
            self.connection.close()
            await self.connection.wait_closed()
            self.connection = None

    async def _run_command(self, command: str) -> str:
        """
        Run a shell command over SSH and return its output.
        """
        if not self.connection:
            await self.connect()
        result = await self.connection.run(command, check=True)
        return result.stdout.strip()

    async def pull_image(self, image_name: str) -> str:
        """
        Pull a Docker image from the registry.
        """
        InputValidator.validate_image_name(image_name)
        await self._run_command(f"docker pull {image_name}")
        return "success"

    async def deploy_container(
        self,
        container_name: str,
        image_name: str,
        env_vars: Optional[Dict[str, str]] = None,
        use_gpu: bool = False
    ) -> str:
        """
        Deploy a new container with optional environment variables and GPU support.
        """
        InputValidator.validate_container_name(container_name)
        InputValidator.validate_image_name(image_name)

        # Format environment variables
        env_cmd = ""
        if env_vars:
            env_cmd = " ".join([f"-e {k}='{v}'" for k, v in env_vars.items()])

        # GPU flag if required
        gpu_flag = "--gpus all" if use_gpu else ""

        # Construct and run the Docker command
        run_command = f"docker run -d --name {container_name} {env_cmd} {gpu_flag} {image_name}"
        await self._run_command(run_command)
        return "success"

    async def start_container(self, container_name: str) -> str:
        """
        Start a Docker container by name.
        """
        InputValidator.validate_container_name(container_name)
        await self._run_command(f"docker start {container_name}")
        return "success"

    async def restart_container(self, container_name: str) -> str:
        """
        Restart a container if running; otherwise, start it.
        """
        InputValidator.validate_container_name(container_name)

        # Check if container is already running
        is_running = await self.is_container_running(container_name)

        if is_running:
            # Restart if currently running
            await self._run_command(f"docker restart {container_name}")
            return f"Container '{container_name}' was running and has been restarted."
        else:
            # Start if it was stopped
            await self._run_command(f"docker start {container_name}")
            return f"Container '{container_name}' was stopped and has been started."

    async def delete_container(self, container_name: str) -> str:
        """
        Forcefully delete a Docker container by name.
        """
        InputValidator.validate_container_name(container_name)
        await self._run_command(f"docker rm -f {container_name}")
        return "success"

    async def stop_container(self, container_name: str) -> str:
        """
        Stop and remove a Docker container by name.
        """
        InputValidator.validate_container_name(container_name)
        await self._run_command(f"docker rm -f {container_name}")
        return "success"

    async def get_container_logs(self, container_name: str, tail: int = 100) -> str:
        """
        Retrieve logs from a container (default: last 100 lines).
        """
        InputValidator.validate_container_name(container_name)
        return await self._run_command(f"docker logs --tail {tail} {container_name}")

    async def is_container_running(self, container_name: str) -> bool:
        """
        Check if a container is currently running.
        """
        InputValidator.validate_container_name(container_name)
        output = await self._run_command(f"docker ps -q -f name=^{container_name}$")
        return bool(output)
