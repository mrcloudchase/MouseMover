import threading
import pyautogui
import random
import time
import PySimpleGUI as sg
from pynput.mouse import Controller

# Create a flag variable to control the loop
should_continue = True


def start_automation():
    # Create a mouse controller
    mouse = Controller()
    # Get screen size
    width, height = pyautogui.size()
    # Start the automation loop
    while should_continue:
        # Move the mouse to a random point within the screen size
        x, y = width*random.random(), height*random.random()
        mouse.position = (x, y)
        time.sleep(3)


# Create the GUI
layout = [[sg.Text('Automate Mouse Movements')],
          [sg.Button('Start'), sg.Button('Stop'), sg.Button('Quit')]]

window = sg.Window('Mouse Automation', layout)

# Main event loop
thread = None
while True:
    event, values = window.read()
    if event == 'Start':
        if thread and thread.is_alive():
            # if the thread is already running, do nothing
            pass
        else:
            # Start the automation in a new thread
            should_continue = True
            thread = threading.Thread(target=start_automation)
            thread.start()
    elif event == 'Stop':
        # Gracefully stop the thread
        should_continue = False
    elif event in (None, 'Quit'):
        # Gracefully stop all threads
        should_continue = False
        if thread:
            thread.join()
        window.close()
        break
    # check for the thread status, if it is not alive then set thread = None
    if thread and not thread.is_alive():
        thread = None
