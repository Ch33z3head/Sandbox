import webbrowser
import requests
import csv
import os
import folium

ipsToken = 'xxxx' #Enter api auth token

def get_ip_geolocation(ip):
    access_token = ipsToken  # Replace with your ipinfo.io access token
    url = f'http://ipinfo.io/{ip}/json?token={access_token}'
    response = requests.get(url)
    data = response.json()
    return {
        'ip': ip,
        'city': data.get('city', 'Unknown'),
        'country': data.get('country', 'Unknown'),
        'org': data.get('org', 'Unknown'),
        'loc': data.get('loc', 'Unknown')
    }

def parse_ips_from_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    ips = set()
    for line in lines:
        if 'remip=' in line:
            start_index = line.find('remip=') + len('remip=')
            end_index = line.find(' ', start_index)
            ip = line[start_index:end_index].strip()
            ips.add(ip)
    return ips

def main():
    file_path = "D:/Workspace//Skunkworks/IpsInfo/error.txt"  # Replace with the path to your log file
    ips = parse_ips_from_log(file_path)
    seen = set()

    # Create a map object
    map_ = folium.Map(location=[0, 0], zoom_start=2)

    with open('ip_geolocation.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'City', 'Country', 'Organization', 'Location'])

        for ip in ips:
            geo_data = get_ip_geolocation(ip)
            if (geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']) not in seen:
                writer.writerow([geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']])
                seen.add((geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']))

                # Extract latitude and longitude from obj
                loc = geo_data['loc'].split(',')
                if len(loc) == 2:
                    latitude, longitude = float(loc[0]), float(loc[1])
                    # Add a marker to the map
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=f"IP: {geo_data['ip']}\nCity: {geo_data['city']}\nCountry: {geo_data['country']}\nOrg: {geo_data['org']}",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(map_)

    # Save the map to an HTML file
    map_.save('ip_geolocation_map.html')    
    webbrowser.open(f'file:///'+ os.path.realpath('ip_geolocation_map.html'))
    
if __name__ == '__main__':
    main()
