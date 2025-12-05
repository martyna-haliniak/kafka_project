import requests
import random
import time

API_URL = "http://127.0.0.1:8000/events"

def generate_event():
    return {
        "user_id": random.randint(1, 1000),
        "action": random.choice(["click", "scroll", "view"]),
        "page": random.choice(["home", "product", "checkout", "search"]),
        "device": random.choice(["mobile", "desktop", "tablet"]),
        "timestamp": int(time.time())
    }

while True:
    data = generate_event()
    print("Sending:", data)
    
    response = requests.post(API_URL, json=data)
    print("API Response:", response.json())

    time.sleep(5)  # send every 5 seconds
