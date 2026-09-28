import psutil


def show_disk_info():
    print("\n" + "=" * 50)
    print("            💾 DISK SPACE MONITOR")
    print("=" * 50)

    partitions = psutil.disk_partitions()

    for partition in partitions:

        try:
            usage = psutil.disk_usage(partition.mountpoint)

            total = usage.total / (1024 ** 3)
            used = usage.used / (1024 ** 3)
            free = usage.free / (1024 ** 3)

            print(f"\n📁 Drive: {partition.mountpoint}")
            print(f"Total: {total:.2f} GB")
            print(f"Used : {used:.2f} GB")
            print(f"Free : {free:.2f} GB")
            print(f"Usage: {usage.percent}%")

        except PermissionError:
            continue


if __name__ == "__main__":
    show_disk_info()