import re

class InputValidator:
    @staticmethod
    def validate_container_name(name: str):
        """
        Validate the Docker container name.

        Allowed characters: letters, numbers, underscores, periods, and hyphens.
        Raises:
            ValueError: If the name contains invalid characters.
        """
        pattern = r'^[a-zA-Z0-9_.-]+$'
        if not re.match(pattern, name):
            raise ValueError(f"Invalid container name: {name}")

    @staticmethod
    def validate_image_name(name: str):
        """
        Validate the Docker image name.

        Allowed characters: letters, numbers, underscores, slashes, colons, periods, and hyphens.
        Raises:
            ValueError: If the name contains invalid characters.
        """
        pattern = r'^[a-zA-Z0-9_/.:@-]+$'
        if not re.match(pattern, name):
            raise ValueError(f"Invalid image name: {name}")

