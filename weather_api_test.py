import requests

# Din API-nyckel från OpenWeatherMap
API_KEY = ''  # Ersätt med din faktiska API-nyckel

# Grund-URL för att hämta väderdata
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Ange staden du vill hämta väderdata för
city = "Alicante"

# Bygg den fullständiga API-anrop URL:n
complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

# Skicka ett GET-anrop till API:et
response = requests.get(complete_url)

# Omvandla svar till JSON-format
data = response.json()

# Skriv ut hela svaret för att se vad som returneras
print(data)

# Kontrollera om svaret innehåller väderdata eller ett fel
if response.status_code == 200:  # 200 innebär att förfrågan lyckades
    if "main" in data:
        # Extrahera huvuddata
        main = data["main"]
        weather_description = data["weather"][0]["description"]

        # Hämta specifik data
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]

        # Skriv ut väderinformation
        print(f"Temperatur i {city}: {temperature}°C")
        print(f"Luftfuktighet i {city}: {humidity}%")
        print(f"Lufttryck i {city}: {pressure} hPa")
        print(f"Väderbeskrivning: {weather_description.capitalize()}")
    else:
        print("Vädret kunde inte hittas, vänligen kontrollera API-anropet.")
else:
    print(f"Fel! Statuskod: {response.status_code}. Meddelande: {data.get('message', 'Ingen ytterligare information.')}")
