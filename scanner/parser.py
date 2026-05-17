def check_security_headers(headers):
    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options"
    ]
    results = {}

    for headers_name in security_headers:
        results[headers_name] = headers.get(headers_name, "Not Found")
    return results    