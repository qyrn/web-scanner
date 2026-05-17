from scanner.fetcher import fetch_headers
from scanner.parser import check_security_headers
from scanner.reporter import print_report

url = "https://example.com"
headers = fetch_headers(url)
results = check_security_headers(headers)
print_report(results, url)