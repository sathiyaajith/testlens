## happy path
* greet
  - utter_greet
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* select_options{"selectoption": "consultation"}
  - action_option_value
  - slot{"selectoption": "consultation"}
* choose_list{"disease": "eyestrain"}
  - action_eye_disease
  - slot{"disease": "eyestrain"}
* get_hours{"hours": "sometimes"}
  - action_time_hours 
  - slot{"hours": "sometimes"}
* get_trouble{"trouble": "rarely"} 
  - action_night_sign
  - slot{"trouble": "rarely"}
* night_headlight{"night": "often"}
  - utter_ask_conclusion
  - slot{"night": "often"} 

## sunglass path
* greet
  - utter_greet
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* sun_options{"sunoption": "sunglasses"}
  - action_glass_brand
  - slot{"sunoption": "sunglasses"}  
* style_glass{"style": "rayban"}  
  - action_style_brand
  - slot{"style": "rayban"}
  - utter_ask_conclusion
  
## powerglass path
* greet
  - utter_greet
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* power_options{"poweroption": "powerglasses"}
  - action_power_wear
  - slot{"poweroption": "powerglasses"}  
* power_specs{"specs": "yes"}
  - action_ask_power
  - slot{"specs": "yes"}
* lens_power{"lenspower": "my power is 2.5 in right eye -2.5 in left eye"}
  - action_vision_problem 
  - slot{"lenspower": "my power is 2.5 in right eye -2.5 in left eye"}  
* eye_problem{"vision": "nearobject"}
  - action_fix_consultation
  - slot{"vision": "nearobject"}
* fix_consultation{"fix": "proceed"}
  - utter_ask_conclusion 


 
