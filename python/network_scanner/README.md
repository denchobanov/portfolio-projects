# Python Network Scanner

A lightweight Python network scanner that verifies host availability, scans configured TCP ports, and generates timestamped scan reports. The project demonstrates practical networking, socket programming, configuration management with JSON, and automated report generation.

## Features

- Checks whether a target host is reachable before scanning
- Scans configurable TCP ports using Python sockets
- Loads scan settings from a `config.json` file
- Configurable timeout and ping count
- Displays open and closed ports
- Generates timestamped scan reports
- Creates the `reports/` directory automatically if it does not exist

## Usage

### Prerequisites

- Python 3
- Standard Python libraries:
  - socket
  - subprocess
  - time
  - os
  - json
  - sys
  - datetime

### Configuration

Edit the `config.json` file to configure:

- Ports to scan
- Connection timeout
- Ping count

### Running the Script

```bash
python3 network_scanner.py <target_ip>
```
