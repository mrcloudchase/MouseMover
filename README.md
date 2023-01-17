# Mouse Mover
This app is a simple GUI application that allows the user to automate mouse movements by clicking on the "Start" button. The mouse will move to random points on the screen at a rate of once every three seconds. The user can also click the "Stop" button to stop the mouse movements and the "Quit" button to close the application. This application is built using the PySimpleGUI library for the GUI and the pynput library for mouse control. This app can be useful for people who wants to automate their mouse movements.


### Requirements:
- Python 3.7 or later
- PySimpleGUI
- PyAutoGUI
- pynput

### Setup:
- Create a Python virtual environment: python3 -m venv venv
- Activate the virtual environment: source venv/bin/activate (macOS/Linux) or venv\Scripts\activate (Windows)
- Install the dependencies: pip install -r requirements.txt

### Running the Application:
- Start the virtual environment: source venv/bin/activate (macOS/Linux) or venv\Scripts\activate (Windows)
- Run the application: python app.py

### Usage:
1. Click the "Start" button to start automating mouse movements.
2. Click the "Stop" button to stop automating mouse movements.
3. Click the "Quit" button to exit the application.

#### Note:
This application will move the mouse cursor randomly on the screen.
The mouse movement is automated at a fixed speed of 3 sec delay between each movement.
You can use this application to simulate human-like mouse movement during long periods of inactivity on your computer.