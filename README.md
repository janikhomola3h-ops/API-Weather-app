# Weather API app
## Description:
- The Weather App is a desktop application built in Python using an external API and several other libraries.
- This application allows users to search for any city on the planet and retrieve current weather information, specifically: general weather conditions (with pre-defined emojis), temperature, visibility, wind speed, and humidity
- The backend and fornend parts are separatly in the same file
### How it works:
#### Backend - done
    - This app is using these Python libraries: PyQt6, sys, requests, os, dotenv
    - Firstly with function get_url app assembles URL with F-String
    - Here is used dotenv library to protect api key
    - After URL assembling app will use requests library to request data from API specifically from "openweathermap"
    - Then these data are converted to JSON again with using requests library 
    - After converting data to JSON are returned to the variable named json
    - After all these steps the specific functions are calling json variable to get specific data from JSON
#### Frontend
    - Application is using PyQt6 library to create UI
        - Specifically here are used window title, window icon, QPushButton, QLineEdit (text bar) and QLabel
    - After entering the city and pushing the search button, the backend logic will call all functions from the backend
    - These functions will return all variables and the function will build text with an f-string and give it to the "final" label
    - Final label will take the string and display it on the UI with alignment to the center

- Main Function
    - Main function is caring about properly closing the app and displaying the UI window
 


#### Error Handling
    - Error handling in this app is very simple
    - App is using a method from requests called raise_for_status
    - The result from this method is validated in the assemble function, and if the result is anything other than code 200, it will send text to the label
    - On the UI, the function will show an error text stating that the user should check the name of the city or check their internet connection
#### How to Run
    - Firstly you have to put your own API key into the file called "api_key.env"
    - Then you just simply run python interpreter like in other python scripts("python project.py")
    - And finally you just enter a city and app will get you the weather from there