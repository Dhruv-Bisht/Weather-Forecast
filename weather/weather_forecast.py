from tkinter import *
import requests
import json
from datetime import datetime
import customtkinter as ct 


#Initialize Window
root = ct.CTk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
    #title of our window
root.title("weather")

ct.set_appearance_mode("dark") 
ct.set_default_color_theme("dark-blue")
    
    # ----------------------Functions to fetch and display weather info
city_value = StringVar()
    
    
def time_format_for_location(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()
    
    
city_value = StringVar()
    
def showWeather():
        #Enter you api key, copies from the OpenWeatherMap dashboard
        api_key = "d9d43191c0f93009e5e4505b3e1cd691"  #sample API
    
        # Get city name from user from the input field (later in the code)
        city_name=city_value.get()
    
        # API url
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    
        # Get the response from fetched url
        response = requests.get(weather_url)
    
        # changing response from json to python readable 
        weather_info = response.json()
    
    
        tfield.delete("1.0", "end")   #to clear the text field for every new output
    
    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    
    
        if weather_info['cod'] == 200:
            kelvin = 273 # value of kelvin
    
    #-----------Storing the fetched values of weather of a city
    
            temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
    
            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)
    
    #assigning Values to our weather varaible, to display as output
            
            weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    
    
        tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
    
    
    
    #------------------------------Frontend part of code - Interface
    

title_heading = ct.CTkLabel(master=root,
                                width=120,
                                height=25,
                                fg_color=("red", "red"),
                                corner_radius=8,
                                text="Weather App",
                                text_font=("Sans Serif",25))
title_heading.place(x=90,y=0)
    
city_head = ct.CTkLabel(master=root,
                                width=120,
                                height=25,
                                fg_color=("red", "red"),
                                corner_radius=8,
                                text="City Name:",
                                text_font=("Sans Serif",15))
city_head.place(x=10,y=50) 
inp_city = ct.CTkEntry(master=root,
                        placeholder_text="City Name",
                        width=180,
                        height=25,
                        border_width=2,
                        corner_radius=10,
                        text_font=("Sans Serif",15),
                        textvariable=city_value
                    )
inp_city.place(x=150,y=50)
    
btn = ct.CTkButton(master=root,
                        command=showWeather,
                        fg_color = ('dodger blue','dodger blue'),
                        text="Check Weather",
                        bg_color=('dodger blue','dodger blue'),
                        text_font=("Times New Roman",15)
                )
btn.place(x=120,y= 100)
    
    #to show output
    
weather_now = ct.CTkLabel(master=root,
                                width=120,
                                height=25,
                                fg_color=("red", "red"),
                                corner_radius=8,
                                text="The Weather is:",
                                text_font=("Arial",15))
weather_now.place(x=10,y=140)
    
tfield = Text(root, width=39, height=9,background="#343638", border=0, foreground="white",font=("Times New Roman",15))
tfield.place(x=10,y=220)
    
root.mainloop() 

