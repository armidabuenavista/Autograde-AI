# test_api.py
import requests
import json

# Test the analyze endpoint
url = "http://localhost:8000/analyze-vehicle/"

with open("data/raw/test_car.jpg", "rb") as f:
    files = {"file": ("test_car.jpg", f, "image/jpeg")}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
if response.status_code == 200:
    print("✅ Success!")
    print(json.dumps(response.json(), indent=2))
else:
    print("❌ Error:", response.text)