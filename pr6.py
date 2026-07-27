import requests
import time


def check_website(url):
    # URL me https nahi hai to add karo
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print("\n" + "=" * 50)
    print("          🌐 WEBSITE STATUS CHECKER")
    print("=" * 50)

    print(f"\n🔍 Checking: {url}")

    try:
        start_time = time.time()

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        end_time = time.time()

        response_time = end_time - start_time

        print("\n✅ Website is reachable!")
        print(f"📡 Status Code : {response.status_code}")
        print(f"⏱️ Response Time: {response_time:.2f} seconds")
        print(f"🔗 Final URL   : {response.url}")

        if 200 <= response.status_code < 300:
            print("🟢 Status: UP")

        elif 300 <= response.status_code < 400:
            print("🟡 Status: REDIRECTED")

        else:
            print("🔴 Status: SERVER ERROR")

    except requests.exceptions.Timeout:
        print("\n⏰ Request timed out.")
        print("🔴 Status: DOWN / TOO SLOW")

    except requests.exceptions.ConnectionError:
        print("\n❌ Could not connect to the website.")
        print("🔴 Status: DOWN")

    except requests.exceptions.RequestException as error:
        print(f"\n❌ Error: {error}")


def main():
    print("🌐 Website Status Checker")

    url = input("\nEnter website URL: ").strip()

    if not url:
        print("❌ URL cannot be empty.")
        return

    check_website(url)


if __name__ == "__main__":
    main()