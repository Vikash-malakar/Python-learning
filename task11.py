import time
from plyer import notification


def set_reminder():
    print("\n" + "=" * 45)
    print("            🔔 DESKTOP REMINDER")
    print("=" * 45)

    title = input("\nReminder title: ").strip()
    message = input("Reminder message: ").strip()

    try:
        seconds = int(input("Reminder after seconds: "))
    except ValueError:
        print("❌ Invalid time.")
        return

    if seconds <= 0:
        print("❌ Time must be greater than 0.")
        return

    print("\n⏳ Waiting...")

    time.sleep(seconds)

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

    print("🔔 Reminder sent!")


if __name__ == "__main__":
    set_reminder()