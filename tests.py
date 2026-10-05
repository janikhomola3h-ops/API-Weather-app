from project import get_weather
from project import get_weather_emoji
from project import get_temperature
from project import get_humidity
from project import get_visibility
from project import get_wind_s
{'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023,
                                                                                                                                                                   'grnd_level': 987}, 'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}


def test_temp():
    assert get_temperature({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023, 'grnd_level': 987}, 'visibility': 10000, 'wind': {
        'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == 14.57


def test_weather():
    assert get_weather({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023, 'grnd_level': 987}, 'visibility': 10000, 'wind': {
                       'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == "Clouds"


def test_emoji():
    assert get_weather_emoji({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023, 'grnd_level': 987}, 'visibility': 10000, 'wind': {
                             'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == "☁️"


def test_hmid():
    assert get_humidity({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023,
                                                                                                                                                                                           'grnd_level': 987}, 'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == 85


def test_vis():
    assert get_visibility({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023,
                                                                                                                                                                                             'grnd_level': 987}, 'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == 10000


def test_wind():
    assert get_wind_s({'coord': {'lon': 14.4208, 'lat': 50.088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 14.57, 'feels_like': 14.3, 'temp_min': 13.49, 'temp_max': 15.64, 'pressure': 1023, 'humidity': 85, 'sea_level': 1023,
                                                                                                                                                                                         'grnd_level': 987}, 'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 290}, 'clouds': {'all': 70}, 'dt': 1789933718, 'sys': {'type': 2, 'id': 2010430, 'country': 'CZ', 'sunrise': 1789879516, 'sunset': 1789923992}, 'timezone': 7200, 'id': 3067696, 'name': 'Prague', 'cod': 200}) == 6.17
