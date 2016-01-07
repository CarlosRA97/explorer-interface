""" GPIO PIN GUI.py --

 UI generated by GUI Builder Build 146 on 2016-01-07 20:17:46 from:
    Z:/Users/Carlos/Documents/explorer-interface/GPIO PIN GUI.ui
 This file is auto-generated.  Only the code within
    '# BEGIN USER CODE (global|class)'
    '# END USER CODE (global|class)'
 and code inside the callback subroutines will be round-tripped.
 The 'main' function is reserved.
"""

from Tkinter import *
from GPIO PIN GUI_ui import GPIO_PIN_GUI

# BEGIN USER CODE global
setmode(BCM)
setwarnings(False)

def on(pin):
	setup(pin, OUT)
	output(pin,1)

def off(pin):
	setup(pin, OUT)
	output(pin,0)

def OnButtonClick(button):
	result = tkMessageBox.askyesno("GPIO PIN","Do you want pin %s turn on?" % button)
	if result:
		on(button)
	else:
		off(button)
# END USER CODE global

class CustomGPIO_PIN_GUI(GPIO_PIN_GUI):
    pass

    # BEGIN CALLBACK CODE
    # ONLY EDIT CODE INSIDE THE def FUNCTIONS.

    # END CALLBACK CODE

    # BEGIN USER CODE class

    # END USER CODE class

def main():
    # Standalone Code Initialization
    # DO NOT EDIT
    try: userinit()
    except NameError: pass
    root = Tk()
    demo = CustomGPIO_PIN_GUI(root)
    root.title('GPIO_PIN_GUI')
    try: run()
    except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
