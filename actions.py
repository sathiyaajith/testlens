from rasa_sdk import Action
from typing import Text
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import FollowupAction
import sqlite3
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import html5lib
from tabulate import tabulate

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["namedetails", "categotydetails", "agedetails"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to donamedetails
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_ask_suggestiondetails", personname=tracker.get_slot('namedetails'),
                                 persongender=tracker.get_slot('categotydetails'),personage=tracker.get_slot('agedetails')
                                 )
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "personname": [self.from_entity(entity="namedetails", intent='name_of_person'),
                     self.from_text()],
            "persongender": [self.from_entity(entity="agedetails", intent="category"),
                        self.from_text()],
            "personage": [self.from_entity(entity="agedetails", intent="years"),
                        self.from_text()]
            
        }
class ActionOptionValue(Action):
    
    def name(self) -> Text:
        return "action_option_value"
         
    def run(self, dispatcher, tracker, domain):
        selectcat = next(tracker.get_latest_entity_values("selectoption"), None)
        print(selectcat)
        dispatcher.utter_message(template="utter_ask_choose")
        print("suggestion slot setted")
        return[SlotSet("selectoption",selectcat)]
        
        
class ActionEyeDisease(Action):
    
    def name(self) -> Text:
        return "action_eye_disease"
         
    def run(self, dispatcher, tracker, domain):
        eye_problem = next(tracker.get_latest_entity_values("disease"), None)
        print(eye_problem )
        dispatcher.utter_message(template="utter_ask_hours")
        print("eye problem slot setted")
        return[SlotSet("disease",eye_problem)]    

class ActionTimeHours(Action):
    
    def name(self) -> Text:
        return "action_time_hours"
         
    def run(self, dispatcher, tracker, domain):
        time_used = next(tracker.get_latest_entity_values("hours"), None)
        print(time_used)
        dispatcher.utter_message(template="utter_ask_trouble")
        print("hour slot setted")
        return[SlotSet("hours",time_used)]    

class ActionNightSign(Action):
    
    def name(self) -> Text:
        return "action_night_sign"
         
    def run(self, dispatcher, tracker, domain):
        night_hours = next(tracker.get_latest_entity_values("trouble"), None)
        print(night_hours)
        dispatcher.utter_message(template="utter_ask_night")
        print("night slot setted")
        return[SlotSet("trouble",night_hours)]  

## Sunglasses path        
        
class ActionGlassBrand(Action):
    
    def name(self) -> Text:
        return "action_glass_brand"
         
    def run(self, dispatcher, tracker, domain):
        sunglass_style = next(tracker.get_latest_entity_values("sunoption"), None)
        print(sunglass_style)
        dispatcher.utter_message(template="utter_ask_style")
        print("sunoption slot setted")
        return[SlotSet("sunoption",sunglass_style)]  


class ActionStyleBrand(Action):
    
    def name(self) -> Text:
        return "action_style_brand"
         
    def run(self, dispatcher, tracker, domain):
        brand_style = next(tracker.get_latest_entity_values("style"), None)
        print(brand_style)
        dispatcher.utter_message(template="utter_ask_sunglasses")
        print("style slot setted")
        return[SlotSet("style",brand_style)]  
        
## Powerglass path

class ActionPowerWear(Action):
    
    def name(self) -> Text:
        return "action_power_wear"
         
    def run(self, dispatcher, tracker, domain):
        powerglass_wear = next(tracker.get_latest_entity_values("poweroption"), None)
        print(powerglass_wear)
        dispatcher.utter_message(template="utter_ask_powerlens")
        print("poweroptions slot setted")
        return[SlotSet("poweroption",powerglass_wear)]  

class ActionAskPower(Action):
    
    def name(self) -> Text:
        return "action_ask_power"
         
    def run(self, dispatcher, tracker, domain):
        powerlens_option = next(tracker.get_latest_entity_values("specs"), None)
        print(powerlens_option)
        dispatcher.utter_message(template="utter_ask_powerdetails")
        print("specs slot setted")
        return[SlotSet("specs",powerlens_option)]        

class ActionVisionProblem(Action):
    
    def name(self) -> Text:
        return "action_vision_problem"
         
    def run(self, dispatcher, tracker, domain):
        vision_option = next(tracker.get_latest_entity_values("lenspower"), None)
        print(vision_option)
        dispatcher.utter_message(template="utter_ask_powerquestion")
        print("lenspower slot setted")
        return[SlotSet("lenspower",vision_option)]                 

class ActionFixConsultation(Action):
    
    def name(self) -> Text:
        return "action_fix_consultation"
         
    def run(self, dispatcher, tracker, domain):
        fix_option = next(tracker.get_latest_entity_values("vision"), None)
        print(fix_option)
        dispatcher.utter_message(template="utter_ask_fixconsultation")
        print("lenspower slot setted")
        return[SlotSet("vision",fix_option)]                 
       

class ActionReport(Action):
    
    def name(self) -> Text:
        return "action_report"
         
    def run(self, dispatcher, tracker, domain):
        night_sol = next(tracker.get_latest_entity_values("night"), None)
        night_ans=SlotSet("night",night_sol)
        night_person = tracker.get_slot("night")
        #dispatcher.utter_message(template="utter_submit")
        dispatcher.utter_message("Report: trouble{}, ".format(night_person))
        return[]        