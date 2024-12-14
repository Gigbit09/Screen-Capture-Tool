Screen Capture Tool
Overview
This Screen Capture Tool is a Python-based application that allows users to record their computer screen.
The tool captures the screen at a specified frame rate (e.g., 60 FPS) and saves the recorded video as an AVI file.
The tool is built using Tkinter for the graphical user interface (GUI), OpenCV for video processing, and PyAutoGUI
for capturing screenshots.

Key Features:
Start and stop screen recording via a simple GUI.
Screen recording saved as an AVI file.
Uses multi-threading to prevent the GUI from freezing during recording.
Captures the screen at a user-defined frame rate (60 FPS by default).
Displays the screen capture live in a window.
Saves the recording in the current working directory (or a user-specified path).


Prerequisites
To run this project, you need the following Python libraries:

PyAutoGUI: Used for capturing screenshots of the screen.
OpenCV: Used for video encoding and frame manipulation.
NumPy: For array manipulation.
Tkinter: For creating the graphical user interface (GUI).
Threading: For handling multi-threading to keep the GUI responsive.
These libraries are not always included by default in Python distributions, so you may need to install them manually.
Please follow the instructions below to install them.

Usage
Starting the Program:
Navigate to the folder where you have saved the Recorder.py file.

Open a terminal or command prompt in that folder.

Run the script with the following command:

bash
Copy code
python Recorder.py
The GUI will appear with two buttons:

Start Recording: Click this to start screen recording.
Stop Recording: Click this to stop the recording.
The recording will be saved as ScreenCapture.avi in the current directory. You can change the location by modifying the output_filename variable in the script.

Stopping the Recording:
Once you click Stop Recording, the recording will be saved, and the GUI will show a confirmation message.


How It Works
Screen Capture: The script uses pyautogui.screenshot() to take screenshots of the screen at regular intervals.
Video Encoding: The screenshots are converted into video frames using OpenCV, which encodes them into an AVI video file.
GUI: A simple graphical user interface (GUI) built with Tkinter allows users to start and stop the recording easily.
Multi-threading: To avoid blocking the main thread and keep the GUI responsive, the recording process runs in a separate thread using Python's threading library.
Important Notes:
The OpenCV library used for video encoding is set to use the XVID codec by default. Ensure that you have the necessary codecs installed if you're having trouble playing the video file.
The screen resolution and frame rate are configurable. By default, the script captures at 1920x1080 resolution and 60 FPS. You can change these values to suit your needs.
Troubleshooting
ModuleNotFoundError: No module named 'cv2': If you encounter this error, make sure that you have installed the opencv-python-headless package using pip install opencv-python-headless.
Error: The function is not implemented: If you get an error like The function is not implemented, it could be due to OpenCV missing GUI support in the headless version. In that case, 
consider using the full opencv-python package instead of opencv-python-headless.
