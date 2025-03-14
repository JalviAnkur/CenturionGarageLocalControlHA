"""Centurion Garage Door Integration."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "centurion_garage"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration using YAML (deprecated)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "cover"))
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "camera"))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the integration when removed."""
    if entry.entry_id in hass.data[DOMAIN]:
        del hass.data[DOMAIN][entry.entry_id]
    return True
