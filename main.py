from scanner.fetcher import fetch_headers
from scanner.parser import check_security_headers
from scanner.reporter import print_report
from scanner.xss import check_reflected_xss

url = "https://example.com"
headers = fetch_headers(url)
results = check_security_headers(headers)
print_report(results, url)
check_reflected_xss("https://0ab200050375f924805af80000b4000a.web-security-academy.net/")