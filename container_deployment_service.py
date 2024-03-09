#!/usr/bin/python3
""" Script contains the logic for deploying containerized applications  """

import docker

class ContainerDeploymentService:
    def __init__(self):
        self.docker_client = docker.from_env()

    def deploy_container(self, application_config):
        """
        Deploy a containerized application based on the provided application_config.

        Parameters:
        - application_config: Dictionary containing configuration parameters for the application.
          Example: {'image': 'my_image', 'port_bindings': {8080: 8080}, 'environment': {'KEY': 'VALUE'}}

        Returns:
        - Container object if deployment is successful, None otherwise.
        """
        try:
            # Pull the Docker image from Docker Hub or a private registry
            image = application_config['image']
            self.docker_client.images.pull(image)

            # Create and start the container
            container = self.docker_client.containers.run(
                image,
                detach=True,
                ports=application_config.get('port_bindings'),
                environment=application_config.get('environment')
            )
            return container
        except Exception as e:
            print(f"Error deploying container: {e}")
            return None

    # Other methods related to container deployment
