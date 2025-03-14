import requests
from homeassistant.components.camera import Camera
from . import DOMAIN

class CenturionGarageCamera(Camera):
    """Camera entity for Centurion Garage Door."""

    def __init__(self, local_ip):
        super().__init__()
        self._ip = local_ip

    def camera_image(self):
        """Fetch camera image."""
        url = f"http://{self._ip}:88"
        response = requests.get(url, timeout=5)
        return response.content
