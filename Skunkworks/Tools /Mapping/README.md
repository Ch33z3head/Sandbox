# IP Geolocation Logger with Map Visualization

This Python script extracts unique IP addresses from a specified log file, retrieves their geolocation information, and visualizes the results on an interactive map. The geolocation data is also saved in a CSV file for further analysis.

## Overview

Using the [ipinfo.io](https://ipinfo.io/products/ip-geolocation-api) API, the script fetches geolocation data for each IP address and uses the `folium` library to create a map with markers indicating the location of each IP.

## Features

- Extracts unique IP addresses from a log file.
- Retrieves geolocation data including city, country, organization, and location coordinates.
- Generates a CSV file containing the geolocation data.
- Creates an interactive HTML map with markers for each IP address's location.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- `folium` library (install via `pip install folium`)

## Setup

1. **Obtain an API Token**: Sign up at [ipinfo.io](https://ipinfo.io) to get your API authentication token.
2. **Install Required Libraries**:
   ```bash
   pip install requests folium
   ```
3. **Update the Script**:
   - Replace `xxxx` in the script with your actual API token.
   - Modify the `file_path` variable to point to your log file.

## Usage

1. Ensure your log file is accessible at the specified path.
2. Run the script:
   ```bash
   python ip_geolocation_logger.py
   ```
3. The output CSV file (`ip_geolocation.csv`) will be created in the same directory, and an HTML file (`ip_geolocation_map.html`) will open in your default web browser.

## Functionality

### `get_ip_geolocation(ip)`

Fetches geolocation data for a given IP address.

- **Parameters**: `ip` (str) - The IP address to look up.
- **Returns**: A dictionary containing the IP, city, country, organization, and location.

### `parse_ips_from_log(file_path)`

Parses the specified log file to extract unique IP addresses.

- **Parameters**: `file_path` (str) - The path to the log file.
- **Returns**: A set of unique IP addresses found in the log.

### `main()`

Coordinates the reading of the log file, fetching of geolocation data, creating the map, and writing to the CSV file.

## Output

- **CSV File**: `ip_geolocation.csv` containing:
  - IP
  - City
  - Country
  - Organization
  - Location

- **HTML File**: `ip_geolocation_map.html` featuring:
  - An interactive map with markers for each IP address location.

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
Example Map Generation of IP locations:

<img width="739" alt="exampleMap" src="https://github.com/user-attachments/assets/b962d641-8227-485b-8504-f891748ad0ac">

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
