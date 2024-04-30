import tkinter as tk
import requests

def get_weather(city):
    api_key = 'e286eec7e6540800e3a60daa6be61120'  # Get your API key from OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        city_name_label.config(text=f'City: {weather_data["name"]}')
        temperature_label.config(text=f'Temperature: {weather_data["main"]["temp"]} °C')
        weather_label.config(text=f'Weather: {weather_data["weather"][0]["description"]}')
    else:
        city_name_label.config(text='City not found')
        temperature_label.config(text='')
        weather_label.config(text='')

def on_submit():
    city = entry.get()
    get_weather(city)

# Create main window
root = tk.Tk()
root.title('Weather Forecast App')

# Create and position widgets
entry = tk.Entry(root, font=('Helvetica', 18))
entry.pack(pady=10)
entry.focus()

submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.pack()

city_name_label = tk.Label(root, font=('Helvetica', 18))
city_name_label.pack(pady=10)

temperature_label = tk.Label(root, font=('Helvetica', 18))
temperature_label.pack()

weather_label = tk.Label(root, font=('Helvetica', 18))
weather_label.pack()

# Start the GUI event loop
root.mainloop()

