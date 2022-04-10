from geopy.geocoders import Nominatim
from suntime import Sun , SunTimeException
from datetime import datetime,timedelta

nat=Nominatim(user_agent="weather")
tomorrow=datetime.now()+timedelta(1)
def weather():
    while True:
        s=input("Do you want to find the sunrise and sunset time of a place ??? : ").lower()
        if s=="yes":
            try:
                find_weather=input("Enter the name of City/Country/State : ").lower()
                loc=nat.geocode(find_weather)
                print(find_weather)

                lat=loc.latitude
                long=loc.longitude
                print(lat,long)
                sun=Sun(lat,long)

                sunrise= sun.get_local_sunrise_time(tomorrow)
                sunset=sun.get_local_sunset_time(tomorrow)
                ss=sunset.strftime("%I:%M")
                sr=sunrise.strftime("%I:%M")
                print(f"The sunset time is {ss}pm and the sunrise time is {sr}am")
            except SunTimeException as e:
                print(e)
        else:
            break

weather()