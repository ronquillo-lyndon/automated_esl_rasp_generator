import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess
import pyautogui
import pyperclip #for copying to clipboard
import time

from Automation.generate_prompt import Rang, generate_prompt, _parse_formatted_prompt
from Utils import user_interface_helper as uih

w, h = uih._get_monitor_size()

def automate_browser(prompt):
    response = ""
    def _open_browser():
        subprocess.Popen([
            r"C:/Program Files/Google/Chrome\Application/chrome.exe",
            "--start-maximized",
            "--profile-directory=Profile 1",   
        ])
        time.sleep(0.5)
    
    def _auto_copy_response(delay):
        nonlocal response
        time.sleep(delay)

        # Click the start
        pyautogui.click((w/2), (h * .40))

        # Scroll down
        for _ in range(50):
            pyautogui.scroll(-500)
            time.sleep(0.05)

        # Hold Shift and click the ends
        pyautogui.keyDown('shift')
        pyautogui.click((w/2), (h * .90))
        pyautogui.keyUp('shift')

        # Copy
        pyautogui.hotkey('ctrl', 'c')

        response = pyperclip.paste()

        pyautogui.click((w * .99), (h * .01))
        time.sleep(0.5)
        pyautogui.click((w * .99), (h * .01))

    def _auto_prompt(prompt):
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'shift', 'n')
        pyautogui.write("https://chatgpt.com/")
        pyautogui.press('enter')
        time.sleep(3)
        pyperclip.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(3)
        pyautogui.press('enter')

        _auto_copy_response(15)

    _open_browser()
    _auto_prompt(prompt)

    return response

if __name__ == "__main__":
    pass
