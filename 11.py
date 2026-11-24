import requests

def check_website_security(url):
    try:
        response = requests.get(url, timeout=10)

        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"HTTPS: {'Yes' if url.startswith('https://') else 'No'}")

        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        print("\nSecurity Headers:")
        for header in security_headers:
            if header in response.headers:
                print(f"✔ {header}: {response.headers[header]}")
            else:
                print(f"✘ {header}: Not Found")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

website = input("Enter website URL (https://example.com): ")
check_website_security(website)
