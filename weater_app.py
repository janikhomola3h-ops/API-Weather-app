from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLineEdit, QLabel
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
import sys
import requests
import os
from dotenv import load_dotenv
# loading secrure API key
load_dotenv("api_key.env")
API_key = os.getenv("API_KEY")
# String for URL


def get_URL(city, API_key):  # building URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    return url


def get_JSON(url):
    Request = requests.get(url)
    list = Request.json()
    Invalid_city_check = requests.get(url)
    Invalid_city_check.raise_for_status()
    return list

    # JSON


def get_weather(json):
    weather = json["weather"][0]["main"]
    return weather


def get_weather_emoji(json):
    emoji_list = {
        "01d": "☀️",
        "01n": "🌙",
        "02d": "🌤️",
        "02n": "☁️",
        "03d": "☁️",
        "03n": "☁️",
        "04d": "☁️",
        "04n": "☁️",
        "09d": "🌧️",
        "10d": "🌦️",
        "11d": "🌩️",
        "13d": "❄️",
        "50d": "🌫️",
    }
    code = json["weather"][0]["icon"]
    output = emoji_list.get(code, "?")
    return output


def get_temperature(json):
    temp = json["main"]["temp"]
    return temp


def get_humidity(json):
    humid = json["main"]["humidity"]
    return humid


def get_visibility(json):
    vis = json["visibility"]
    return vis


def get_wind_s(json):
    wind = json["wind"]["speed"]
    return wind


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Title + icon - Main Window
        self.setWindowTitle("Weather App by HudbaBezZvuku")
        self.setWindowIcon(QIcon("images/icon.png"))
        # Width and height on start + locking that geometry
        self.setGeometry(200, 200, 400, 600)
        # Locking geometry
        self.setFixedHeight(600)
        self.setFixedWidth(400)

        # Search button
        self.button = QPushButton("Search for weather...", self)
        self.button.setGeometry(27, 200, 350, 100)

        # Search text bar settings
        self.text_bar = QLineEdit(self)
        self.text_bar.setPlaceholderText("Enter a city...")
        self.text_bar.setGeometry(27, 70, 350, 100)
        self.text_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # results get from API text box
        self.final = QLabel(self)
        self.final.setGeometry(27, 280, 350, 280)
        self.final.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.final.setFont(QFont("Arial", 20, QFont.Weight.Bold))

        # connecting button with backend
        self.button.clicked.connect(self.assemble)

    def assemble(self):  # this function is connecting backend and GUI
        try:
            city = self.text_bar.text()
            city = city.strip().title()
            url = get_URL(city, API_key)
            json = get_JSON(url)

        except requests.exceptions.HTTPError:  # invalid city handling
            self.final.setText("Check internet\n or \n Invalid City")
        else:
            # getting info from API
            weather = get_weather(json)
            emoji = get_weather_emoji(json)
            temp = get_temperature(json)
            humid = get_humidity(json)
            vis = get_visibility(json)
            wind = get_wind_s(json)
            # assambling text to display it on the GUI
            text = f"City: {city}\nWeather: {weather}\n{emoji}\n Temerature: {temp}\n Humidity: {humid}\n Visibility: {vis}\n Strength of wind: {wind}"
            # puting text to the final
            self.final.setText(text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
