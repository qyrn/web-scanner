def print_report(results, url):
    print(f"=== Security Headers Report for {url} ===")
    for header, value in results.items():
        if value == "Not Found":
            print(f"[MISSING] {header}: Not Found (Potential Security Risk)")
        else:
            print(f"[OK] {header}: {value}")