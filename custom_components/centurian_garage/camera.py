import requests
from homeassistant.components.camera import Camera
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Centurion Garage Camera entity from a config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([CenturionGarageCamera(data["local_ip"])])

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
