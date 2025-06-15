# mercury/alerts/alert_manager.py
import requests
import yaml

# Load configuration
with open("config.yaml") as f:
    config = yaml.safe_load(f)

API_KEY = config['fast2sms_api_key']
PHONE = config['alert_phone']

def send_alert(message):
    print(f"[ALERT] {message}")
    try:
        payload = {
            'sender_id': 'FSTSMS',
            'message': message,
            'language': 'english',
            'route': 'p',  # Use 'q' for promotional, 'p' for transactional
            'numbers': PHONE
        }
        headers = {
            'authorization': API_KEY,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache'
        }
        response = requests.post("https://www.fast2sms.com/dev/bulk", data=payload, headers=headers)
        print("SMS sent:", response.json())
    except Exception as e:
        print("Failed to send SMS via Fast2SMS:", e)
