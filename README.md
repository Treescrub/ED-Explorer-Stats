# ED Explorer Stats

A Python application to parse player journals and display interesting exploring stats for Elite Dangerous.

Windows is the only currently supported platform.

**Intended for ED Horizons/Odyssey, data from Legacy may or may not work**

## Install

To install from source, use `pip install .`.
To install from PyPI, use `pip install ed-explorer-stats`.

## Usage

Run `explorer-stats` to list all stat groups that can be executed.

To execute a stat group, pass the name as a subcommand.

For example: `explorer-stats visited_systems`

## Dependencies

* colorama

## Development

To develop with an editable install, run `pip install --editable .`.

## Planned Features
* Stat caching to reduce journal reading

## Todo
* Support Linux
* Upload to PyPI