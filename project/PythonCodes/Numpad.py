# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: Numpad puzzle for the final gate opening phase of the project
# Course: IST440W
# Author: Dhruv Parekh, Harshil Patel, Avi Patel
# Date Developed: 2/24/2022
# Last Date Changed: 3/27/2022
# Revision: 6

from m5stack import *
from m5stack_ui import *
from uiflow import *
import urequests
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xcacaca)
servo1 = unit.get(unit.SERVO, unit.PORTA)


Ans = None



touch_button0 = M5Btn(text='1', x=12, y=123, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button1 = M5Btn(text='2', x=90, y=121, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button2 = M5Btn(text='3', x=167, y=123, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button3 = M5Btn(text='4', x=12, y=162, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button = M5Btn(text='5', x=92, y=161, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button5 = M5Btn(text='6', x=167, y=161, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button6 = M5Btn(text='7', x=13, y=203, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button7 = M5Btn(text='8', x=93, y=204, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button8 = M5Btn(text='9', x=170, y=203, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button10 = M5Btn(text='Clear', x=250, y=162, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button11 = M5Btn(text='0', x=248, y=203, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button4 = M5Btn(text='Enter', x=250, y=123, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label1 = M5Label('Server Data', x=110, y=96, color=0x000, font=FONT_MONT_14, parent=None)
Equal = M5Label('=', x=186, y=56, color=0x000, font=FONT_MONT_24, parent=None)
Answer = M5Label('Text', x=230, y=56, color=0x000, font=FONT_MONT_24, parent=None)
label0 = M5Label('Enter Answer To The Problem Below', x=18, y=10, color=0x000, font=FONT_MONT_16, parent=None)
problem = M5Label('( 2 * 6 ) - 4', x=36, y=56, color=0x000, font=FONT_MONT_24, parent=None)



def touch_button4_pressed():
  global Ans
  servo1.write_angle(180)
  wait(3)
  servo1.write_us(0)
  pass
touch_button4.pressed(touch_button4_pressed)

def touch_button0_pressed():
  global Ans
  print('')
  Answer.set_text('1')
  label0.set_text('Try Again!')
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button1_pressed():
  global Ans
  print('')
  Answer.set_text('2')
  label0.set_text('Try Again!')
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button2_pressed():
  global Ans
  print('')
  Answer.set_text('3')
  label0.set_text('Try Again!')
  pass
touch_button2.pressed(touch_button2_pressed)

def touch_button3_pressed():
  global Ans
  print('')
  Answer.set_text('4')
  label0.set_text('Try Again!')
  pass
touch_button3.pressed(touch_button3_pressed)

def touch_button_pressed():
  global Ans
  print('')
  Answer.set_text('5')
  label0.set_text('Try Again!')
  pass
touch_button.pressed(touch_button_pressed)

def touch_button5_pressed():
  global Ans
  print('')
  Answer.set_text('6')
  label0.set_text('Try Again!')
  pass
touch_button5.pressed(touch_button5_pressed)

def touch_button6_pressed():
  global Ans
  print('')
  Answer.set_text('7')
  label0.set_text('Try Again!')
  pass
touch_button6.pressed(touch_button6_pressed)

def touch_button7_pressed():
  global Ans
  print('')
  Answer.set_text('8')
  label0.set_text('Press Enter to open the gate')
  pass
touch_button7.pressed(touch_button7_pressed)

def touch_button8_pressed():
  global Ans
  print('')
  Answer.set_text('9')
  label0.set_text('Try Again!')
  pass
touch_button8.pressed(touch_button8_pressed)

def touch_button10_pressed():
  global Ans
  print('')
  Answer.set_hidden(True)
  pass
touch_button10.pressed(touch_button10_pressed)

def touch_button11_pressed():
  global Ans
  print('')
  Answer.set_text('0')
  label0.set_text('Try Again!')
  pass
touch_button11.pressed(touch_button11_pressed)

def touch_button10_pressed():
  global Ans
  print('')
  label0.set_text('Number Cleared!!')
  Answer.set_hidden(True)
  label1.set_hidden(True)
  pass
touch_button10.pressed(touch_button10_pressed)

def touch_button7_released():
  global Ans
  try:
    req = urequests.request(method='POST', url='http://192.168.1.178:5000/logs',json={'TeamName':'Team4','PuzzleName':'NumpadPuzzle','Status':'Complete'}, headers={'Content-Type':'application/json'})
    label1.set_text('Puzzle Data Sent')
  except:
    label1.set_text('Data Send Failed')
  pass
touch_button7.released(touch_button7_released)

def touch_button10_released():
  global Ans
  wait(3)
  Answer.set_hidden(False)
  pass
touch_button10.released(touch_button10_released)


problem.set_hidden(False)
Ans = 8
