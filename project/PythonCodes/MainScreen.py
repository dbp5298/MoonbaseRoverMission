# Project: IST440WSP22 Capstone M5Stack
# Purpose Details: Welcome screen and main screen for the project
# Course: IST440W
# Author: Charles Kirschner, Dhruv Parekh, Avi Patel, Harshil Patel
# Date Developed: 2/27/2022
# Last Date Changed: 04/01/2022
# Revision: 5


from m5stack import *
from m5stack_ui import *
from uiflow import *
import urequests

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


countdown = None



touch_button_okay = M5Btn(text='Okay', x=123, y=138, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
image_win = M5Img("res/WinMainScreen.PNG", x=75, y=60, parent=None)
send_data = M5Btn(text='Send Data', x=63, y=60, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label0 = M5Label('Mission Complete!', x=41, y=16, color=0x000, font=FONT_MONT_26, parent=None)
label_countdown = M5Label('Timer', x=188, y=60, color=0x0a14ba, font=FONT_MONT_30, parent=None)
image_logo = M5Img("res/IST440W - Logo.png", x=47, y=10, parent=None)
label_cnt_num = M5Label('Text', x=200, y=96, color=0xdd0808, font=FONT_MONT_28, parent=None)
label_start = M5Label('START', x=113, y=196, color=0x000, font=FONT_MONT_30, parent=None)
touch_button_go = M5Btn(text='Go', x=15, y=29, w=70, h=30, bg_c=0xFFFFFF, text_c=0x5dcd54, font=FONT_MONT_14, parent=None)
touch_button_help = M5Btn(text='Help', x=15, y=71, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button_reset = M5Btn(text='Reset', x=13, y=121, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button_stop = M5Btn(text='Stop', x=13, y=173, w=70, h=30, bg_c=0xFFFFFF, text_c=0xc62b2b, font=FONT_MONT_14, parent=None)
label_help_info = M5Label('Text', x=0, y=0, color=0x000, font=FONT_MONT_12, parent=None)

from numbers import Number



# dictates what elements of the UI are shown and not shown
def touch_button_stop_pressed():
  global countdown
  image_logo.set_hidden(True)
  image_win.set_hidden(True)
  label_start.set_hidden(True)
  label_countdown.set_hidden(False)
  touch_button_go.set_hidden(False)
  touch_button_help.set_hidden(False)
  touch_button_reset.set_hidden(False)
  touch_button_stop.set_hidden(False)
  timerSch.stop('timer1')
  pass
touch_button_stop.pressed(touch_button_stop_pressed)

# Shows the user the help bubble as well as the okay button to get out of it.
def touch_button_help_pressed():
  global countdown
  label_help_info.set_hidden(False)
  label_start.set_hidden(True)
  touch_button_go.set_hidden(True)
  touch_button_help.set_hidden(True)
  touch_button_reset.set_hidden(True)
  touch_button_stop.set_hidden(True)
  touch_button_okay.set_hidden(False)
  label_help_info.set_text('Collect the drone wreckage and return in time!')
  label_countdown.set_hidden(True)
  label_cnt_num.set_hidden(True)
  image_win.set_hidden(True)
  pass
touch_button_help.pressed(touch_button_help_pressed)

# Returns the user back to the Timer menu.
def touch_button_go_pressed():
  global countdown
  touch_button_help.set_hidden(False)
  touch_button_go.set_hidden(False)
  touch_button_reset.set_hidden(False)
  touch_button_stop.set_hidden(False)
  touch_button_okay.set_hidden(True)
  image_logo.set_hidden(True)
  label_countdown.set_hidden(False)
  label_cnt_num.set_hidden(False)
  label_cnt_num.set_text(str(countdown))
  timerSch.run('timer1', 1000, 0x00)
  pass
touch_button_go.pressed(touch_button_go_pressed)

# Returns the user back to the Timer menu.
def touch_button_okay_pressed():
  global countdown
  label_help_info.set_hidden(True)
  touch_button_go.set_hidden(False)
  touch_button_help.set_hidden(False)
  touch_button_reset.set_hidden(False)
  touch_button_stop.set_hidden(False)
  touch_button_okay.set_hidden(True)
  image_win.set_hidden(True)
  pass
touch_button_okay.pressed(touch_button_okay_pressed)

# Returns the user back to the Timer menu.
def touch_button_reset_pressed():
  global countdown
  countdown = 0
  timerSch.stop('timer1')
  label_cnt_num.set_text(str(countdown))
  pass
touch_button_reset.pressed(touch_button_reset_pressed)

# function to send final data to the server
def send_data_pressed():
  global countdown
  try:
    req = urequests.request(method='POST', url='http://192.168.1.178:5000/logs',json={'TeamName':'Team4','PuzzleName':'SafeLanding','Status':'Complete'}, headers={'Content-Type':'application/json'})
    label0.set_hidden(False)
  except:
    label0.set_text('FAIL')
  pass
send_data.pressed(send_data_pressed)


# Initiate the main screen by hiding welcome screen
# components and showing main screen components
def buttonB_wasPressed():
  global countdown
  image_logo.set_hidden(True)
  label_start.set_hidden(True)
  touch_button_go.set_hidden(False)
  touch_button_help.set_hidden(False)
  touch_button_reset.set_hidden(False)
  touch_button_stop.set_hidden(False)
  touch_button_okay.set_hidden(True)
  label_countdown.set_hidden(True)
  label_cnt_num.set_hidden(True)
  image_win.set_hidden(True)
  label0.set_hidden(True)
  send_data.set_hidden(True)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global countdown
  image_logo.set_hidden(True)
  image_win.set_hidden(False)
  label_start.set_hidden(True)
  label_help_info.set_hidden(True)
  label_countdown.set_hidden(True)
  label_cnt_num.set_hidden(True)
  touch_button_go.set_hidden(True)
  touch_button_reset.set_hidden(True)
  touch_button_stop.set_hidden(True)
  touch_button_okay.set_hidden(True)
  touch_button_help.set_hidden(True)
  send_data.set_hidden(False)
  label0.set_hidden(True)
  pass
btnC.wasPressed(buttonC_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global countdown
  countdown = (countdown if isinstance(countdown, Number) else 0) + 1
  label_cnt_num.set_text(str(countdown))
  pass


image_logo.set_hidden(False)
label_start.set_hidden(False)
image_win.set_hidden(True)
send_data.set_hidden(True)
touch_button_go.set_hidden(True)
touch_button_help.set_hidden(True)
touch_button_reset.set_hidden(True)
touch_button_stop.set_hidden(True)
label_help_info.set_hidden(True)
touch_button_okay.set_hidden(True)
label_countdown.set_hidden(True)
label_cnt_num.set_hidden(True)
label0.set_hidden(True)
timerSch.run('timer1', 1000, 0x00)
