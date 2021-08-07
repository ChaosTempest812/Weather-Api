import tkinter as tk
import requests

root = tk.Tk()
root.geometry("350x350")
root.title("Weather API")


fillerlabel = tk.Label(bg="#43bcd1")
fillerlabel.place(relx = 0.1, rely = 0.27, relwidth = 0.85, relheight = 0.5)



def search(entry):
    city = entry
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f28e3683317b7da551f035ca2c55c81b"

    fillerlabel = tk.Label(bg="#43bcd1")
    fillerlabel.place(relx = 0.1, rely = 0.27, relwidth = 0.85, relheight = 0.5)

    try:
        data = requests.get(api).json()
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
            
        temperature_in_kelvin = data["main"]["temp"]
        temperature = (temperature_in_kelvin - 273.15) * 9/5 + 32
            
        finaltext = tk.Label(text="Temperature:", bg="#43bcd1")
        finaltext.place(relx = 0.11, rely = 0.3)

        finaltext2 = tk.Label(text = int(temperature), bg="#43bcd1")
        finaltext2.place(relx = 0.35, rely = 0.3)
            
        weatherlabel = tk.Label(text = "Weather:", bg="#43bcd1")
        weatherlabel.place(relx = 0.11, rely = 0.4)
            
        weatherlabel2 = tk.Label(text = weather, bg="#43bcd1")
        weatherlabel2.place(relx = 0.28, rely = 0.4)

        weatherlabel3 = tk.Label(text = humidity, bg="#43bcd1")
        weatherlabel4 = tk.Label(text = "Humidity (%):", bg = "#43bcd1")

        weatherlabel3.place(relx = 0.33, rely = 0.5)
        weatherlabel4.place(relx = 0.11, rely = 0.5)

        weatherlabel5 = tk.Label(text = "Wind speed (mph): ", bg="#43bcd1")
        weatherlabel6 = tk.Label(text = wind_speed, bg="#43bcd1")

        weatherlabel5.place(relx = 0.11, rely = 0.6)
        weatherlabel6.place(relx = 0.4, rely = 0.6)
                                          
    except Exception as e:
        finaltext = tk.Label(text="Error...", bg="#43bcd1")
        finaltext.place(relx = 0.11, rely = 0.3)

    

frame = tk.Frame(root, bg = "#43bcd1", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.85, relheight=0.15)

Search_Bar = tk.Entry(frame, border = 3, font=40)
Search_Bar.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.6)

Search_Button = tk.Button(frame, text="Search", command=lambda: search(Search_Bar.get()))
Search_Button.place(relx = 0.7, rely = 0 , relwidth = 0.3, relheight = 1)




root.mainloop
