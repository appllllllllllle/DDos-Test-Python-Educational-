import requests
import time
#MADE BY appllllllllllle
 
url = "URL"  # Put your URL

def M():
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.0000000001)

if __name__ == "__main__":
    M()
