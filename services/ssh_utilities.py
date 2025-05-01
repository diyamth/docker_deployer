import asyncssh
import asyncio
import re
from typing import Optional, Dict

class SSHClient:
    def __init__(
        self,
        host: str,
        username: str,
        password: Optional[str] = None,
        private_key: Optional[str] = None,
        known_hosts: Optional[str] = None
    ):
        # SSH connection parameters
        self.host = host
        self.username = username
        self.password = password
        self.private_key = private_key
        self.known_hosts = known_hosts

    async def __aenter__(self):
        """
        Asynchronous context manager entry.
        Establishes an SSH connection using provided credentials.
        """
        conn_params = {
            "host": self.host,
            "username": self.username,
            "known_hosts": self.known_hosts or None,
            "login_timeout": 10,
        }

        # Choose authentication method: private key or password
        if self.private_key:
            conn_params["client_keys"] = [self.private_key]
        elif self.password:
            conn_params["password"] = self.password

        # Open the SSH connection
        self.conn = await asyncssh.connect(**conn_params)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
        Asynchronous context manager exit.
        Closes the SSH connection gracefully.
        """
        self.conn.close()
        await self.conn.wait_closed()

    async def run(self, command: str, retries: int = 3, delay: int = 2) -> str:
        """
        Execute a shell command over SSH with retry support.

        Args:
            command: Shell command to execute.
            retries: Number of retry attempts.
            delay: Delay between retries (in seconds).

        Returns:
            Command output as a trimmed string.

        Raises:
            Exception: If command fails after all retry attempts.
        """
        for attempt in range(retries):
            try:
                result = await self.conn.run(command, check=True)
                return result.stdout.strip()
            except asyncssh.ProcessError as e:
                # Raise an error after final failed attempt
                if attempt == retries - 1:
                    raise Exception(f"Command failed after {retries} attempts: {str(e)}")
                await asyncio.sleep(delay)
