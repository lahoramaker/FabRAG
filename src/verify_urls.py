import csv
import requests
from urllib.parse import urlparse
import sys

def is_url_available(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_urls(file_path):
    available_urls = []
    unavailable_urls = []

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 3:
                week, session_name, url = row[0], row[1], row[2]
                if is_url_available(url):
                    available_urls.append((week, session_name, url))
                else:
                    unavailable_urls.append((week, session_name, url))

    print("Available URLs:")
    for url in available_urls:
        print(f"Week {url[0]}: {url[1]} - {url[2]}")

    print("\nUnavailable URLs:")
    for url in unavailable_urls:
        print(f"Week {url[0]}: {url[1]} - {url[2]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_urls(file_path)