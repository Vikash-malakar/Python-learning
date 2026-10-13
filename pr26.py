import cv2
from pyzbar.pyzbar import decode


def scan_qr():
    camera = cv2.VideoCapture(0)

    print("📷 Camera started.")
    print("QR code camera ke saamne rakho.")
    print("Press Q to exit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("❌ Camera access failed.")
            break

        qr_codes = decode(frame)

        for qr in qr_codes:
            data = qr.data.decode("utf-8")

            print("\n" + "=" * 40)
            print("✅ QR CODE FOUND")
            print("=" * 40)
            print(f"Data: {data}")
            print("=" * 40)

            points = qr.polygon

            if len(points) >= 4:
                for i in range(len(points)):
                    start = points[i]
                    end = points[(i + 1) % len(points)]

                    cv2.line(
                        frame,
                        (start.x, start.y),
                        (end.x, end.y),
                        (0, 255, 0),
                        3
                    )

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    scan_qr()