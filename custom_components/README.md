# Centurion Garage Local Control (Home Assistant Integration)

This is a custom integration for controlling **Centurion Garage Doors** via a local API.

## Installation

### 1. Manual Installation
1. Download the `custom_components/centurion_garage` folder.
2. Copy it to your Home Assistant `config/custom_components/` directory.
3. Restart Home Assistant.
4. Add the integration in Home Assistant UI.

### 2. Installation via HACS
1. Open HACS in Home Assistant.
2. Go to **Integrations** > **Custom Repositories**.
3. Add: https://github.com/yourgithubusername/CenturionGarageLocalControlHA
Set category to **Integration**.
4. Install the integration and restart Home Assistant.

## Configuration
1. In Home Assistant, go to **Settings** → **Devices & Services** → **Add Integration**.
2. Select **Centurion Garage**.
3. Enter your **Local IP** and **API Key**.

## Features
- Open, close, and stop the garage door.
- Stream camera feed from `http://<local_ip>:88`.

## Support
For issues, report them at [GitHub Issues](https://github.com/JalviAnkur/CenturionGarageLocalControlHA/issues).
