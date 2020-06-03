# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        city = tracker.get_slot("city")
        import urllib, json, urllib.request
        locationurl = "https://us1.locationiq.com/v1/search.php?key=008f52be0602de&q=" + city + "&format=json"
        with urllib.request.urlopen(locationurl) as url:
            s = url.read()
            location = json.loads(s)
            lat = location[0]['lat']
            longitude = location[0]['lon']
        url = "https://api.ipgeolocation.io/timezone?apiKey=12d640cded414f098c8f7452c2a5d34c&lat=" + lat + "&long=" + longitude
        with urllib.request.urlopen(url) as url:
            s = url.read()
            location = json.loads(s)

        dispatcher.utter_message(text="The Time Zone of " + str(city) + " is "+ str(location['timezone_offset']) + ' ' + location['timezone'] + ' with current date and time as ' + location['date_time'])

        return []
