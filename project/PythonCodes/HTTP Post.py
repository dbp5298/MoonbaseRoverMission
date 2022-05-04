# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: Sending a JSON dump from the M5Stack to the Raspberry PI server
# Course: IST440W
# Author: Charles Kirschner
# Date Developed: 3/24/2022
# Last Date Changed: 3/29/2022
# Revision: 2

from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
import urequests

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




wifiCfg.doConnect('wifi ssid', 'wifi password')

label0 = M5Label('Text', x=138, y=83, color=0x000, font=FONT_MONT_14, parent=None)


try:
  req = urequests.request(method='POST', url='http://192.168.1.178:5000/logs',json={'TeamName':'Team4','PuzzleName':'placeholder','Status':'complete'}, headers={'Content-Type':'application/json'})
  label0.set_text(str(req.status_code))
except:
  label0.set_text('Fail')