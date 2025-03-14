import voluptuous as vol
from homeassistant import config_entries
from . import DOMAIN

CONF_IP = "local_ip"
CONF_KEY = "api_key"

class CenturionGarageConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Centurion Garage."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Centurion Garage", data=user_input)
        
        data_schema = vol.Schema(
            {
                vol.Required(CONF_IP): str,
                vol.Required(CONF_KEY): str,
            }
        )
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

