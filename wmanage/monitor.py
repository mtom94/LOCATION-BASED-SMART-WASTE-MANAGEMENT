import io
#import cv2
import numpy as np
import os
import sqlite3
from datetime import datetime
from datetime import date
import paho.mqtt.client as mqtt
import threading

client= mqtt.Client()
# s_status='Empty'
def insert_to_db(a, b):
    try:
        sqliteConnection1 = sqlite3.connect('db.sqlite3')
        cursor1 = sqliteConnection1.cursor()
        print("Successfully Connected to SQLite")

        # Assuming the table name is 'GarbageB' and 'g_fill' is the column to be updated
        cursor1.execute("UPDATE w_app_garbageb SET g_fill = ? WHERE g_id = ?", (b, a))

        sqliteConnection1.commit()
        sqliteConnection1.close()
        print("Successfully updated g_fill column in SQLite for g_id:", a)

    except sqlite3.Error as error:
        print("Failed to update g_fill column in SQLite:", error)


##############  mqtt start ############
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("smartbin2024")

def on_message(client, userdata, msg):##############
    print(msg.topic+" -- "+str(msg.payload))

    payload_str=str(msg.payload)[2:-1]       
    components = payload_str.split(', ')

    bin_id = components[0].split(':')[1]
    percentage = components[1]

    a = bin_id
    b = percentage

    print("BinID:",a)
    print("Percentage:",b)
    insert_to_db(a,b)




client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

def run(n):
    client.loop_forever()
t1 = threading.Thread(target=run, args=(10,))
t1.start()
t1.join()

##############  mqtt end ############

