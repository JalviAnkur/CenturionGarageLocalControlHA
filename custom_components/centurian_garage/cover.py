import requests
from homeassistant.components.cover import CoverEntity, SUPPORT_OPEN, SUPPORT_CLOSE, SUPPORT_STOP
from . import DOMAIN

class CenturionGarageDoor(CoverEntity):
    """Representation of a Centurion Garage Door."""

    def __init__(self, local_ip, api_key):
        """Initialize the garage door."""
        self._ip = local_ip
        self._key = api_key
        self._state = None

    @property
    def name(self):
        return "Centurion Garage Door"

    @property
    def is_closed(self):
        return self._state == "closed"

    @property
    def supported_features(self):
        return SUPPORT_OPEN | SUPPORT_CLOSE | SUPPORT_STOP

    def open_cover(self, **kwargs):
        """Open the garage door."""
        url = f"http://{self._ip}/api?key={self._key}&door=open"
        requests.post(url)
        self._state = "open"
        self.schedule_update_ha_state()

    def close_cover(self, **kwargs):
        """Close the garage door."""
        url = f"http://{self._ip}/api?key={self._key}&door=close"
        requests.post(url)
        self._state = "closed"
        self.schedule_update_ha_state()

    def stop_cover(self, **kwargs):
        """Stop the garage door."""
        url = f"http://{self._ip}/api?key={self._key}&door=stop"
        requests.post(url)
        self._state = "stopped"
        self.schedule_update_ha_state()
