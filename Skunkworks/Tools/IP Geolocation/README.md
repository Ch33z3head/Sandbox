# IP Geolocation Logger

This Python script retrieves geolocation information for IP addresses found in a specified log file and saves the data to a CSV file.

## Overview

The script uses the [ipinfo.io](https://ipinfo.io/products/ip-geolocation-api) API to fetch geolocation data for each unique IP address present in a log file. The output is stored in a CSV format, making it easy to analyze and share.

## Features

- Parses a log file to extract unique IP addresses.
- Retrieves geolocation data for each IP address.
- Saves the results in a CSV file, including city, country, organization, and location.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Setup

1. **Obtain an API Token**: Sign up at [ipinfo.io](https://ipinfo.io) to get your API authentication token.
2. **Install Required Libraries**:
   ```bash
   pip install requests
   ```
3. **Update the Script**:
   - Replace `xxxx` in the script with your actual API token.
   - Update the `file_path` variable with the path to your log file.

## Usage

1. Place your log file in the specified location.
2. Run the script:
   ```bash
   python ip_geolocation_logger.py
   ```
3. The output will be saved in `ip_geolocation.csv` in the same directory.

## Functionality

### `get_ip_geolocation(ip)`

Fetches geolocation data for a given IP address.

- **Parameters**: `ip` (str) - The IP address to look up.
- **Returns**: A dictionary containing IP, city, country, organization, and location.

### `parse_ips_from_log(file_path)`

Parses the specified log file to extract IP addresses.

- **Parameters**: `file_path` (str) - The path to the log file.
- **Returns**: A set of unique IP addresses found in the log.

### `main()`

Coordinates the reading of the log file, fetching of geolocation data, and writing to the CSV file.

## Output

The resulting `ip_geolocation.csv` file will contain the following columns:

- IP
- City
- Country
- Organization
- Location

## Example

Input (from log file):
```
... remip=192.0.2.1 ...
... remip=203.0.113.42 ...
```

Output (in `ip_geolocation.csv`):
```
IP, City, Country, Organization, Location
192.0.2.1, Example City, EX, Example Org, 40.7128,-74.0060
203.0.113.42, Another City, AN, Another Org, 34.0522,-118.2437
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
