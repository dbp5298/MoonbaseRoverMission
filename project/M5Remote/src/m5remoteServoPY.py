from m5stack import *
from m5ui import *
from uiflow import *
import time
import urequests
import unit
remoteInit()
setScreenColor(0x222222)
servo_4 = unit.get(unit.SERVO, unit.PORTB)
servo_5 = unit.get(unit.SERVO, unit.PORTC)
servo_2 = unit.get(unit.SERVO, unit.PORTA)






label0 = M5TextBox(78, 112, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(250, 224, "4", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(139, 224, "START", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(59, 224, "5", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label6 = M5TextBox(45, 131, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label7 = M5TextBox(60, 151, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(6, 6, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label8 = M5TextBox(6, 0, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
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

def buttonC_wasReleased():
  # global params
  try:
    req = urequests.request(method='POST', url='http://192.168.1.178:5000/logs',json={'TeamName':'Team4','PuzzleName':'RoverStartupPuzzle','Status':'Complete'}, headers={'Content-Type':'application/json'})
    label8.setText('201')
  except:
    label8.setText('400')
  pass
btnC.wasReleased(buttonC_wasReleased)

# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: M5Remote application (remote control on phone to control M5Rover)
# Course: IST440W
# Author: Dhruv Parekh
# Date Developed: 2/24/2022
# Last Date Changed: 3/18/2022
# Revision: 4
def _remote_Forward():
  global servo_4, servo_5, servo_2 
  servo_4.write_us(1410)
  servo_5.write_us(1550)

def _remote_Reverse():
  global servo_4, servo_5, servo_2 
  servo_4.write_us(1550)
  servo_5.write_us(1410)

def _remote_Left():
  global servo_4, servo_5, servo_2 
  servo_4.write_us(1410)
  servo_5.write_us(1410)

def _remote_Right():
  global servo_4, servo_5, servo_2 
  servo_4.write_us(1550)
  servo_5.write_us(1550)

def _remote_Stop():
  global servo_4, servo_5, servo_2 
  servo_4.write_us(0)
  servo_5.write_us(0)

def _remote_Home():
  global servo_4, servo_5, servo_2 
  lcd.clear()
  label5.show()
  label4.show()
  label0.show()
  label6.show()
  label7.show()
  label3.show()
  label1.show()
  label2.show()

def _remote_Grip():
  global servo_4, servo_5, servo_2 
  servo_2.write_angle(180)

def _remote_Release():
  global servo_4, servo_5, servo_2 
  servo_2.write_angle(0)


label4.setText('Solve the following to access the rover ')
label5.setText('remote controls')
label0.setText('Click Start in middle')
label6.setText('Count the number of RGB flashes')
label7.setText('Select the correct number')
label8.hide()
servo_4.write_us(0)
servo_5.write_us(0)

# command to move the rover forward

# command to move the rover backward/reverse

# command to turn the rover left

# command to turn the rover right

# command to stop the rover

# displays the QR code on M5Stack for the remote control connection for new user

# Describe this function...

# Describe this function...