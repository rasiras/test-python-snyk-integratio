import requests

def main():
    url = 'https://example.com'
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Request succeeded')
    else:
        print('Request failed')

if __name__ == "__main__":
    main()
