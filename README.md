# OctoPrint-MGSetup

This plugin provides general setup and configuration interfaces for control of the MakerGear M3 Single and Independent Dual Extruder printers.

## Features

- **Firmware Management**: Update and configure MakerGear printer firmware
- **Network Configuration**: Manage WiFi, hostname, and network settings
- **Printer Calibration**: Tools for bed leveling, probe calibration, and offset adjustments
- **System Maintenance**: Access to maintenance scripts, logs, and diagnostics
- **Registration**: Printer registration and support interfaces

## Requirements

- **Python**: 3.7+ (fully compatible with Python 3.13)
- **OctoPrint**: 1.3.0 or higher
- **Platform**: Raspberry Pi (Raspbian/Raspberry Pi OS) recommended

## Installation

### Recommended: Install from Plugin Repository

We strongly recommend only using full Release versions of this plugin, as those have been fully tested and released for general use.

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager) by searching for "MGSetup".

### Development: Install Latest Version

To install the absolute latest, currently testing version:

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager) or manually using this URL:

    https://github.com/ouchinou/MakerGear_OctoPrint_Setup/archive/master.zip


## Configuration

The plugin provides several configuration tabs in the OctoPrint interface:

- **Setup Tab**: Main configuration and calibration interface
- **Maintenance Tab**: System diagnostics and maintenance tools
- **Support Tab**: Access to logs and support resources
- **Registration**: Printer registration interface

## Python 3 Migration

This plugin has been fully migrated to Python 3 and is compatible with:
- Python 3.7+
- Python 3.13 (latest tested version)

The codebase follows Python best practices including:
- UTF-8 encoding for all text file operations
- Context managers (`with` statements) for resource management
- PEP 8 code style compliance
- Proper exception handling

## Development

### Project Structure

```
MakerGear_OctoPrint_Setup/
├── octoprint_mgsetup/           # Main plugin package
│   ├── __init__.py              # Core plugin logic (1620 lines)
│   ├── static/                  # CSS, JS, images, scripts
│   │   ├── css/                 # Stylesheets
│   │   ├── js/                  # JavaScript files
│   │   ├── maintenance/         # Maintenance scripts and configs
│   │   │   ├── scripts/         # Python/shell scripts
│   │   │   ├── cura/            # Cura profiles
│   │   │   ├── gcode/           # Test G-code files
│   │   │   └── system/          # System configuration files
│   │   └── img/                 # Images and icons
│   ├── templates/               # Jinja2 templates
│   ├── logs/                    # Log files directory
│   └── video/                   # Video resources
├── setup.py                     # Plugin installation script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

### Running Code Quality Tools

The project uses several tools to maintain code quality:

```bash
# Format code with autopep8
autopep8 --in-place --recursive .

# Upgrade Python syntax
pyupgrade --py37-plus **/*.py

# Modernize Python 2 to 3 (already applied)
modernize -w .
```

## Support

For issues, questions, or support:
- **Issues**: [GitHub Issues](https://github.com/ouchinou/MakerGear_OctoPrint_Setup/issues)
- **Original Repository**: [MakerGear/MakerGear_OctoPrint_Setup](https://github.com/MakerGear/MakerGear_OctoPrint_Setup)
- **MakerGear Support**: Contact MakerGear customer support

## License

See LICENSE file for details.

## Version History

### v0.4.1.0 (Current)
- Full Python 3 compatibility (Python 3.7 - 3.13)
- Code quality improvements (PEP 8 compliance)
- Enhanced error handling and logging
- UTF-8 encoding for all file operations
- Removed deprecated Python 2 constructs

### Previous Versions
- v0.3.1.x: Python 2 legacy versions
- See [Releases](https://github.com/ouchinou/MakerGear_OctoPrint_Setup/releases) for full history

## Credits

Developed by the MakerGear Development Team for the MakerGear M3 printer series.

