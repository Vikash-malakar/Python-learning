import requests


def shorten_url(long_url):

    api_url = "https://tinyurl.com/api-create.php"

    params = {
        "url": long_url
    }

    try:
        response = requests.get(
            api_url,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            return response.text

        return None

    except requests.exceptions.RequestException:
        return None


def main():

    print("\n" + "=" * 45)
    print("            🔗 URL SHORTENER")
    print("=" * 45)

    long_url = input("\nEnter long URL: ").strip()

    if not long_url:
        print("❌ URL cannot be empty.")
        return

    if not long_url.startswith(
        ("http://", "https://")
    ):
        print("❌ Please enter a valid URL.")
        return

    print("\n⏳ Creating short URL...")

    short_url = shorten_url(long_url)

    if short_url:
        print("\n✅ URL shortened successfully!")
        print(f"\nOriginal URL:")
        print(long_url)

        print(f"\nShort URL:")
        print(short_url)

    else:
        print("\n❌ Could not shorten the URL.")


if __name__ == "__main__":
    main()