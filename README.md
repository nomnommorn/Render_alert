# Render_alert
A simple Blender addon that plays a notification sound when rendering is complete. Never miss a finished render again!

## Features

- Plays a system-specific notification sound after a render finishes.
- Simple on/off controls in the Render Properties panel.
- Compatible with Windows, macOS, and Linux.

## Installation

1. Download the `render_alert.py` file from this repository.
2. Open Blender, go to `Edit > Preferences > Add-ons`.
3. Click `Install...` and select the downloaded `render_alert.py` file.
4. Enable the addon by checking the checkbox next to `Render Complete Alert`.

## Usage

1. Go to the Render Properties panel in Blender (the panel with the render settings).
2. Find the "Render Complete Alert" section at the bottom of the panel.
3. Click **Enable Alert** to activate the notification.
4. Render your scene as usual.
5. When the render completes, you will hear a notification sound.

To disable the alert, click **Disable Alert** in the same panel.

## Supported Platforms

- **Windows:** Uses the system's default notification sound.
- **macOS:** Plays the built-in `Glass.aiff` sound.
- **Linux:** Uses the default system sound via `paplay`.

## Contributing

Contributions and improvements are welcome! Feel free to submit issues or pull requests.

## License

This addon is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
