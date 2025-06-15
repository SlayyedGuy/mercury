# 🛡️ Mercury: Smart CCTV Surveillance System

**Mercury** is an intelligent CCTV security system built in Python that uses DeepFace for facial recognition. It detects people in real-time from a camera feed, identifies known individuals, and triggers alerts for unknown people.

## 🚀 Features

- 🔍 Real-time face recognition using DeepFace
- 📷 Support for webcam and IP camera feeds
- 🚨 Instant alerts for unknown faces
- 🧠 Configurable known face database
- 📊 Optional web dashboard with Flask (extendable)
- 📁 Modular and clean project structure

## 📂 Project Structure

mercury/
├── main.py # Main entry point
├── config.yaml # Configuration: camera URL, alert settings, known faces path
├── requirements.txt # Python dependencies

├── camera/
│ ├── camera_stream.py # Read and manage camera feeds
│ └── frame_processor.py # Preprocess and resize frames

├── detection/
│ ├── person_detector.py # Detect people using YOLO/MediaPipe
│ └── unusual_activity.py # Detect loitering, intrusion, or abnormal motion

├── recognition/
│ ├── face_recognizer.py # Compare faces to known encodings
│ └── face_encoder.py # Encode known face images into vectors

├── alerts/
│ ├── alert_manager.py # Send alerts (email, push notifications, etc.)
│ └── log_event.py # Log events with timestamps and frames

├── ui/
│ ├── dashboard.py # Optional: Local or web dashboard for viewing
│ └── visual_overlay.py # Draw boxes and labels on detected faces/objects

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/mercury-cctv.git
cd mercury-cctv
```
