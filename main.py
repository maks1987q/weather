from datetime import datetime
import sqlite3
import requests

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT,
        temperature TEXT
    )
""")

url = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true"
response = requests.get(url)
data = response.json()
temp = str(data["current_weather"]["temperature"]) + "°C"

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute(
    "INSERT INTO weather (datetime, temperature) VALUES (?, ?)", (now, temp)
)

conn.commit()
conn.close()

print("Готово, дані збережено!")