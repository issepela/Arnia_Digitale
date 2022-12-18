# Arnia_Digitale

## inital set of file to let the beehive coomuicate with a private webserver through TheThingsNetwork cloud    

LORA_arnia.ino: Arduino sketch to send a random number every 20 min (input your own keys)  
MQTT_TTN_arnia.py: Python script to subscibe to the MQTT channel provided by ttn  
Arnia_Digitale_db.py:  Python code to extract info from the JSON received from ttn and store it into a Sqlite sb  
