import pyautogui
import webbrowser
import time
import requests

url = "https://passport.twitch.tv/login"
data = {
    "username": "prisoneer_",
    "password": "Arne86503"
}

webbrowser.open("https://www.twitch.tv/login")
response = requests.post(url, data=data)
