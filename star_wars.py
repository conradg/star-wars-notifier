#Python 3.4, started writing on 18th of October 2015 after getting back from Belgium/Netherlands trip with Elle

import requests, time

#Get the API token for Yo account "STARWARSIMAXUK"
f = open("../yo_api_token.txt", 'r')
api_token = f.read()
f.close()

# We look out for this snippet at the bookingURL to see whether booking is open
watchword = """<a href="#showtimes" class="btn orange"> Book Now</a>"""
bookingURL  = "http://www.odeon.co.uk/films/star_wars_the_force_awakens/15866"

def isBookingOpen (ww,url) :
    return ww in requests.get(url).text


# Yo all subscribers with the URL to book tickets
def yo_all():
    requests.post("https://api.justyo.co/yoall/", data={'api_token': api_token, 'link': bookingURL})


# Send a yo to IFTTT which triggers a notification of my choice on my phone
def yo_ifttt():
    requests.post("https://api.justyo.co/yo/", data={'api_token': api_token, 'username': "IFTTT"})


while (not isBookingOpen(watchword,bookingURL)):
    print ("Booking not open yet\n")
    time.sleep(30) # wait 30 seconds and check again

if isBookingOpen(watchword, bookingURL):
    yo_all()
    yo_ifttt()
    exit ()

