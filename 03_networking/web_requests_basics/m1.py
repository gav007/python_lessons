import requests

url = "https://api.github.com/events"

headers = {
    "User-Agent": "gav-api-practice/1.0",
    "Accept": "application/json"
}

r = requests.get(url, headers=headers, timeout=5)

print("Status:", r.status_code)

data = r.json()

print("Type of data:", type(data))
print("Number of items:", len(data))

first_item = data[0]

print("First item type:", first_item.get("type"))
print("First item id:", first_item.get("id"))
