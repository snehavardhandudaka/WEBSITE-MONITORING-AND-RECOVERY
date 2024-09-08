import requests
import sys

def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = "http://example.com"  # Replace with your website URL
    status = check_website(url)
    if status == 200:
        print("Website is up.")
    else:
        print("Website is down.")
        sys.exit(1)

