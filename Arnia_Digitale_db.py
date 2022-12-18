# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:14:38 2022

@author: a.pessi
"""
import os
import sqlite3

con = sqlite3.connect('Arnia_Digitale.db')
con.execute("CREATE TABLE Test_data(ID integer PRIMARY KEY,Arnia text,Time text,Valore integer)")
con.commit()
con.close()

con = sqlite3.connect('Arnia_Digitale.db')
con.execute("insert into Test_data(Arnia,Time,Valore) values('A1','2022_12_17_15_25_10','4');")
con.commit()
con.close()

import json
import datetime

x=json.loads(a.payload)
DT= x['uplink_message']['rx_metadata'][0]['received_at']
DT=DT.split(".")[0].replace("T"," ")
V= x['uplink_message']['f_cnt']
Arnia=x['end_device_ids']['device_id']


con = sqlite3.connect('Arnia_Digitale.db')
res=con.execute("select id from ARNIE where device_id='eui-a8610a33342c6815'")
id_arnia=res.fetchall()[0][0]

con = sqlite3.connect('Arnia_Digitale.db')
sqlstr = "INSERT INTO Test_data(Arnia,Time,Valore) values({},'{}', {});".format(id_arnia, DT,V)
res=con.execute(sqlstr)
con.commit()

