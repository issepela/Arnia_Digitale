# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 07:42:52 2022

@author: a.pessi
"""

#import context 
import datetime
import paho.mqtt.subscribe as subscribe

topic="v3/coderdojobrianza-lora@ttn/devices/eui-a8610a33342c6815/up"

print("subscribe")
while(True):
    m = subscribe.simple(topics=['#'], 
                         hostname="eu1.cloud.thethings.network", 
                         port=1883, 
                         auth={'username':zzz,'password':kkk}, 
                         msg_count=2)
    print(datetime.datetime.now())
    for a in m:
        print(a.topic)
        print(a.payload)
        
        
        