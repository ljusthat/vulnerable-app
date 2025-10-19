import requests

def main():
    r = requests.get("https://httpbin.org/get")
    print("Status:", r.status_code)

if __name__ == "__main__":
    main()
