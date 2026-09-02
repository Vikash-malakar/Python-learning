import requests

API_URL = "https://newsdata.io/api/1/latest"


def get_news(api_key, country="in"):
    params = {
        "apikey": api_key,
        "country": country,
        "language": "en"
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            return []

        data = response.json()

        if data.get("status") != "success":
            print("❌ News fetch nahi ho saki.")
            return []

        return data.get("results", [])

    except requests.exceptions.Timeout:
        print("⏰ Request timeout ho gaya.")
        return []

    except requests.exceptions.RequestException as error:
        print(f"❌ Network error: {error}")
        return []


def display_news(news):
    if not news:
        print("❌ Koi news nahi mili.")
        return

    print("\n" + "=" * 70)
    print("                    📰 LATEST NEWS")
    print("=" * 70)

    for number, article in enumerate(news[:10], start=1):
        title = article.get("title", "No title")
        source = article.get("source_name", "Unknown source")
        description = article.get("description") or "No description"

        print(f"\n{number}. {title}")
        print(f"   🏢 Source: {source}")
        print(f"   📝 {description[:150]}...")
        print("-" * 70)


def main():
    print("\n" + "=" * 50)
    print("             📰 PYTHON NEWS READER")
    print("=" * 50)

    api_key = input("\nEnter your NewsData API key: ").strip()

    if not api_key:
        print("❌ API key required.")
        return

    print("\n⏳ Fetching latest news...")

    news = get_news(api_key)

    display_news(news)


if __name__ == "__main__":
    main()