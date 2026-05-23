# SURVILLANCE CAMERA WITH PERSON DETECTION

# Overview
    This project is an AI-powered surveillance system with person detection and gives alert using SMS.

# Hardware Component Used
    ESP32-CAM
    RHYX M21-45 camera 
    USB to TTL 
    2x Servo 
    2-axis Gimbal(3D print)

# Software used
    YOLOv8 for person detection
    Twilio SMS alert system

# Pin connections
    1.USB to TTL and ESP32-CAM
         5V - 5V
         GND - GND
         TXD - UORXD 
         RXD - UOTXD

    ADDITION - IO0 - GND (ESP32-CAM)

    2.SERVO MOTOR and ESP32-CAM
        Pan Servo (Horizontal)- GPIO 12
        Tilt Servo (Vertical) - GPIO 13

    Note: Power servo using external battery(2x)

# Working

    This project follows an integrated IoT and AI-based approach to build a smart surveillance system using an ESP32-CAM module, a 2-axis servo-based gimbal which is 3D printed and a Python-based YOLOv8 object detection model. 
    
    Initially, the ESP32-CAM is configured using Laptop or local system with the help of USB to TTL that capture real-time video frames in grayscale format and stream them over a WiFi access point. The camera continuously serves images through an HTTP endpoint, which is accessed by a Python script running on a local system.

    In parallel, the YOLOv8 model processes each incoming frame to detect the presence of a person in real time. Once a person is detected, the system calculates the position of the detected object within the frame and sends corresponding control signals to the ESP32 to adjust the pan and tilt servos, enabling automatic tracking of the target.

    At the same time, when a person is detected, an alert mechanism is triggered using the Twilio SMS API, which sends a notification message containing the detection alert along with the ESP32 camera IP address for live monitoring. 

    The servo motors are controlled through GPIO pins on the ESP32, allowing smooth horizontal and vertical movement of the camera mounted on a 3D-printed gimbal. 

    This combination of real-time image processing, embedded control, and cloud-based communication enables an efficient, low-cost surveillance system capable of object detection, tracking, and remote alerting in a fully automated manner.

    (Refer block diagram)

# Conclusion

    Hence the IP address will be shared to the registered person through SMS.The person detection is successfully achieved with the help of YOLOv8 model.

    (Refer output screenshots)  



