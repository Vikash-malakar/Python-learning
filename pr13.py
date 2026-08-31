import platform
import socket
import os
import sys
import getpass
from datetime import datetime


def get_system_info():

    print("\n" + "=" * 55)
    print("             💻 SYSTEM INFORMATION")
    print("=" * 55)

    print("\n🖥️ Operating System")
    print("-" * 30)
    print(f"OS            : {platform.system()}")
    print(f"OS Version    : {platform.version()}")
    print(f"OS Release    : {platform.release()}")

    print("\n⚙️ Processor")
    print("-" * 30)
    print(f"Processor     : {platform.processor()}")
    print(f"Architecture  : {platform.machine()}")
    print(f"CPU Cores     : {os.cpu_count()}")

    print("\n🐍 Python")
    print("-" * 30)
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Path   : {sys.executable}")

    print("\n🌐 Network")
    print("-" * 30)

    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print(f"Hostname      : {hostname}")
        print(f"IP Address    : {ip_address}")

    except socket.error:
        print("Network information unavailable.")

    print("\n👤 User")
    print("-" * 30)
    print(f"Username      : {getpass.getuser()}")

    print("\n⏰ Current Time")
    print("-" * 30)
    print(
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    print("\n" + "=" * 55)
    print("             ✅ INFORMATION COMPLETE")
    print("=" * 55)


if __name__ == "__main__":
    get_system_info()