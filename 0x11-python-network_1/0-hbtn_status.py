url = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
    
    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)

