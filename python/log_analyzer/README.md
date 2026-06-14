# Python Log Analyzer

A lightweight Python tool that analyzes log files and generates reports containing system statistics, recurring errors, and security-related events. Designed as a practical project for troubleshooting, log analysis, and basic security monitoring.

## Features

- Counts ERROR, WARNING, and INFO log entries
- Detects recurring errors
- Identifies the most common error
- Detects failed login attempts
- Generates timestamped reports
- Creates a security summary
- Automatically creates a reports directory if it does not exist

## Usage

### Prerequisites

- Python 3
- Standard Python libraries:
  - os
  - datetime

### Running the Script

```bash
python3 log_analyzer.py
