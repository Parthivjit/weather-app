import requests
import json
import tkinter as tk
from tkinter import messagebox

# WEATHER API FUNCTION 
def get_weather():
    city = city_entry.get()
    if city.strip() == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key=257b8ca6d24d467e9d5133435251611&q={city}"

    try:
        r = requests.get(url)

        if r.status_code != 200:
            messagebox.showerror("Error", f"City '{city}' not found!")
            return

        data = r.json()

        temp = data['current']['temp_c']
        desc = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind = data['current']['wind_kph']
        location = f"{data['location']['name']}, {data['location']['country']}"

        # CHOOSING THE EMOJIS FOR THE WEATHER CONDITION
        d = desc.lower()
        if "rain" in d:
            emoji = "🌧️"
        elif "cloud" in d:
            emoji = "☁️"
        elif "sun" in d or "clear" in d:
            emoji = "☀️"
        elif "snow" in d:
            emoji = "❄️"
        else:
            emoji = "🌫️"

        # Update UI  
        location_label.config(text=location)
        emoji_label.config(text=emoji)
        temp_label.config(text=f"{temp}°C")
        condition_label.config(text=desc)
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind} km/h")

    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather.")


#  INITIALISING TKINTER UI 
app = tk.Tk()
app.title("Weather App")
app.geometry("380x450")
app.configure(bg="#1e1e1e")

# CODES FOR THE INPUT PORTION
city_entry = tk.Entry(app, font=("Arial", 16), width=18, justify="center")
city_entry.pack(pady=20)

search_btn = tk.Button(app, text="Search Weather", font=("Arial", 14), command=get_weather)
search_btn.pack()

# CODES FOR THE OUTPUT PORTION
emoji_label = tk.Label(app, text="❔", font=("Arial", 70), bg="#1e1e1e", fg="white")
emoji_label.pack(pady=10)

location_label = tk.Label(app, text="", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
location_label.pack()

temp_label = tk.Label(app, text="", font=("Arial", 40), bg="#1e1e1e", fg="cyan")
temp_label.pack()

condition_label = tk.Label(app, text="", font=("Arial", 18), bg="#1e1e1e", fg="yellow")
condition_label.pack(pady=5)

humidity_label = tk.Label(app, text="", font=("Arial", 14), bg="#1e1e1e", fg="lightblue")
humidity_label.pack()

wind_label = tk.Label(app, text="", font=("Arial", 14), bg="#1e1e1e", fg="lightgreen")
wind_label.pack()

app.mainloop()
