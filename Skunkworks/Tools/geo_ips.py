import requests
import csv

ipsToken = 'xxxx' #Enter api auth token

def get_ip_geolocation(ip):
    access_token = ipsToken # Replace with your ipinfo.io access token
    url = f'http://ipinfo.io/{ip}/json?token={access_token}'
    response = requests.get(url)
    data = response.json()
    return {
        'ip': ip,
        'city': data.get('city', 'Unknown'),
        'country': data.get('country', 'Unknown'),
        'org': data.get('org', 'Unknown'),
        'loc': data.get('loc', 'Unknown')}

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
    file_path = "C:/Users/Downloads/error.txt"  # Replace with the path to your log file
    ips = parse_ips_from_log(file_path)
    seen = set()

    with open('ip_geolocation.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'City', 'Country', 'Organization', 'Location'])

        for ip in ips:
            geo_data = get_ip_geolocation(ip)
            if (geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']) not in seen:
                writer.writerow([geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']])
                seen.add((geo_data['ip'], geo_data['city'], geo_data['country'], geo_data['org'], geo_data['loc']))

if __name__ == '__main__':
    main()
