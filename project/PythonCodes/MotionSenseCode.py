# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: Code for the PIR motion sensor to detect rover at endzone
# Course: IST440W
# Author: Dhruv Parekh
# Date Developed: 3/24/2022
# Revision: 1


from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
pir_1 = unit.get(unit.PIR, unit.PORTA)


label0 = M5Label('Text', x=142, y=95, color=0x000, font=FONT_MONT_14, parent=None)


while True:
  if (pir_1.state) == 1:
    while (pir_1.state) == 1:
      label0.set_text('Rover Has Landed')
  else:
    label0.set_text('N/A')
  wait_ms(2)