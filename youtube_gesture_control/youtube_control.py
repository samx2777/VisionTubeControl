import pyautogui
import cv2
import numpy as np
import time
import os

# Gesture → Action mapping
GESTURE_ACTIONS = {
    "Thumb Up": "Volume Up",
    "Thumb Down": "Volume Down",
    "Index + Middle": "Play/Pause",
    "Palm Open": "Fullscreen",
    "Index Point": "Mute",
    "Scroll Up": "Scroll Up",
    "Scroll Down": "Scroll Down"
}

def execute_action(gesture_name):
    """
    Execute YouTube action based on gesture name.
    """
    action = GESTURE_ACTIONS.get(gesture_name)
    if not action:
        return

    if action == "Volume Up":
        pyautogui.press("up")
    elif action == "Volume Down":
        pyautogui.press("down")
    elif action == "Play/Pause":
        pyautogui.press("k") # 'k' is more reliable than 'space' in browser
    elif action == "Mute":
        pyautogui.press("m")
    elif action == "Fullscreen":
        pyautogui.press("f")
    elif action == "Scroll Up":
        pyautogui.scroll(300) # Scroll up
    elif action == "Scroll Down":
        pyautogui.scroll(-300) # Scroll down

    print(f"Executed Action: {action}")
