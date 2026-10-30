# PortSwigger Lab: DOM XSS in document.write sink using source location.search

## Lab Description
- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Apprentice
- **Objective:** Perform a DOM-based cross-site scripting attack that calls the `alert` function.

## Vulnerability Analysis
This lab contains a DOM-based XSS vulnerability in the search query tracking functionality. The application uses the `document.write` sink (JavaScript function) to write data from the `location.search` source (URL parameter) directly into the HTML page. Because the input is written inside an HTML attribute (`<img src="...">`), we need to break out of the attribute context to execute JavaScript.

## Exploitation Steps
1. Performed a search for `test` and opened DevTools to inspect the DOM.
2. Noticed the input was reflected inside an `<img>` tag's `src` attribute:
   ```html
   <img src="/resources/images/tracker.gif?searchTerms=test">
   ```
3. Injected the following payload into the search bar to break out of the attribute and inject a new tag:
   ```html
   "><svg onload=alert(5)>
   ```
4. The payload closed the `src` attribute (`"`), closed the `<img>` tag (`>`), and created a new `<svg>` tag with an `onload` event.
5. The browser executed the JavaScript, triggering the `alert(5)` popup.

## Evidence

### Payload Injection
![DOM XSS Payload](screenshots/07-dom-xss-payload.png)

### DOM Manipulation in DevTools
![DOM XSS DevTools](screenshots/08-dom-xss-devtools.png)

### Alert Execution (PoC)
![DOM XSS Alert](screenshots/09-dom-xss-alert.png)

### Lab Solved
![DOM XSS Solved](screenshots/10-dom-xss-solved.png)

## Mitigation
To prevent DOM XSS, the application must use safe DOM APIs (like `textContent`) instead of `document.write` or `innerHTML`. Additionally, the URL parameters (sources) should be validated and sanitized before being passed to any sinks.