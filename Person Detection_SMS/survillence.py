import requests
import numpy as np
import cv2
import time

from PIL import Image
from io import BytesIO

from ultralytics import YOLO
from twilio.rest import Client

# =====================================
# ESP32 CAMERA URL
# =====================================

ESP32_IP = "192.168.4.1"

IMAGE_URL = f"http://{ESP32_IP}/capture"

# =====================================
# TWILIO SETTINGS
# =====================================

account_sid = "SID"
auth_token = "TOKEN"

twilio_number = "TWILIO_NUMBER"
your_number = "+91xxxxxxxxxx"

client = Client(account_sid, auth_token)

# =====================================
# LOAD YOLO MODEL
# =====================================

model = YOLO("yolov8n.pt")

# =====================================
# SMS TIMER (ANTI-SPAM)
# =====================================

last_sms_time = 0

# =====================================
# SEND SMS FUNCTION
# =====================================

def send_sms():

    global last_sms_time

    # Prevent continuous SMS spam
    if time.time() - last_sms_time < 30:
        return

    try:

        message = client.messages.create(

            body=
            "PERSON DETECTED!\n\n"
            "Intruder detected in surveillance area.\n\n"
            "Open Camera:\n"
            f"http://{ESP32_IP}",

            from_=twilio_number,

            to=your_number
        )

        print("SMS SENT")
        print(message.sid)

        last_sms_time = time.time()

    except Exception as e:

        print("SMS ERROR:", e)

# =====================================
# MAIN LOOP
# =====================================

while True:

    try:

        # =================================
        # GET IMAGE FROM ESP32
        # =================================

        response = requests.get(IMAGE_URL, timeout=5)

        # Convert image bytes to image
        img = Image.open(BytesIO(response.content))

        # Convert to numpy array
        frame = np.array(img)

        # =================================
        # GRAYSCALE → BGR
        # =================================

        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # =================================
        # YOLO DETECTION
        # =================================

        results = model(frame)

        person_detected = False

        for r in results:

            boxes = r.boxes

            for box in boxes:

                cls = int(box.cls[0])

                # PERSON CLASS = 0
                if cls == 0:

                    person_detected = True

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    conf = float(box.conf[0])

                    label = f"Person {conf:.2f}"

                    # =========================
                    # DRAW RECTANGLE
                    # =========================

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # =========================
                    # SHOW LABEL
                    # =========================

                    cv2.putText(
                        frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )

        # =================================
        # SEND SMS IF PERSON DETECTED
        # =================================

        if person_detected:

            print("PERSON DETECTED!")

            send_sms()

        # =================================
        # SHOW CAMERA WINDOW
        # =================================

        cv2.imshow("ESP32 AI Surveillance", frame)

        # PRESS Q TO EXIT
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:

        print("ERROR:", e)

        time.sleep(1)

# =====================================
# CLEANUP
# =====================================

cv2.destroyAllWindows()