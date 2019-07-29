# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import date


class ActionHowOldYouAre(Action):    

    def __years_old(self):
        days_in_year = 365.2425    
        age = (date.today() - date(2019, 7, 23)).days
        
        if(age < 30):
            return str(age) + " dias"
            
        if(age < days_in_year):
            month = int(age * 0.0329)
            return str(month) + " mes" + ("es" if month > 1 else "")
        
        years = int(age / days_in_year)
        
        return str(years) + " ano" + ( "s" if years > 1 else "")

    def name(self) -> Text:
        return "action_how_old_you_are"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message('Tenho {} de vida, e subindo'.format(self.__years_old()))

        return []
    
