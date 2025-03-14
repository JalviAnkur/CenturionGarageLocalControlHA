"""Centurion Garage Door Integration."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "centurion_garage"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration using YAML (deprecated)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data

    # Forward setup to the cover and camera platforms
    await hass.config_entries.async_forward_entry_setup(entry, "cover")
    await hass.config_entries.async_forward_entry_setup(entry, "camera")

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the integration when removed."""
    await hass.config_entries.async_forward_entry_unload(entry, "cover")
    await hass.config_entries.async_forward_entry_unload(entry, "camera")

    if entry.entry_id in hass.data[DOMAIN]:
        del hass.data[DOMAIN][entry.entry_id]

    return True
