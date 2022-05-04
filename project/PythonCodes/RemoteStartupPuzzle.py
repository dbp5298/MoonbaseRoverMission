# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: M5Remote Startup Puzzle to access the rover controls
# Course: IST440W
# Author: Dhruv Parekh
# Date Developed: 3/13/2022
# Last Date Changed: 3/18/2022
# Revision: 3


from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)


label0 = M5TextBox(78, 112, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(250, 224, "4", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(139, 224, "START", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(59, 224, "5", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label6 = M5TextBox(45, 131, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label7 = M5TextBox(60, 151, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(6, 6, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label5 = M5TextBox(6, 28, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  # global params
  speaker.sing(233, 1)
  rgb.setColorAll(0xff0000)
  wait(1)
  rgb.setColorAll(0x000000)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  wait(1)
  rgb.setColorAll(0xff0000)
  wait(0.7)
  rgb.setColorAll(0x000000)
  wait(0.7)
  rgb.setColorAll(0x3333ff)
  wait(0.7)
  rgb.setColorAll(0x000000)
  wait(0.7)
  rgb.setColorAll(0x33ff33)
  wait(0.7)
  rgb.setColorAll(0x000000)
  wait(0.7)
  rgb.setColorAll(0xcc33cc)
  wait(0.7)
  rgb.setColorAll(0x000000)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  # global params
  speaker.sing(932, 1)
  lcd.print('Scan QR Code on a phone', 65, 10, 0xff0000)
  lcd.print('to access the M5Rover remote', 45, 215, 0xff0000)
  label0.hide()
  label1.hide()
  label2.hide()
  label3.hide()
  label4.hide()
  label5.hide()
  label6.hide()
  label7.hide()
  # displays the QR code on M5Stack for the remote control connection
  lcd.qrcode('http://flow-remote.m5stack.com/?remote=702121469186146304', 72, 32, 176)
  pass
btnC.wasPressed(buttonC_wasPressed)

label4.setText('Solve the following to access the rover ')
label5.setText('remote controls')
label0.setText('Click Start in middle')
label6.setText('Count the number of RGB flashes')
label7.setText('Select the correct number')