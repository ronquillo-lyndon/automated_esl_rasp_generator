import psutil
import webbrowser
import pygetwindow as gw
from screeninfo import get_monitors
import pyautogui
import pyperclip #for copying to clipboard
import time

from generate_prompt import Rang, generate_prompt, _parse_formatted_prompt

#from playwright.sync_api import sync_playwright


BROWSERS = {
    "chrome": ["chrome.exe", "google-chrome", "chrome"],
    "firefox": ["firefox.exe", "firefox"],
    "edge": ["msedge.exe", "msedge"],
    "opera": ["opera.exe", "opera"],
    "brave": ["brave.exe", "brave"],
}

def _is_browser_running(browser):
    names = BROWSERS.get(browser.lower(), [])
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() in names:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

def _get_monitor_size():
    width = 0
    height = 0
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height

    return width, height


def automate_browser(prompt):
    def _open_browser():
        webbrowser.open("https://www.google.com")
        while True:
            windows = gw.getWindowsWithTitle("Google")
            if windows:
                windows[0].activate()
                break
            time.sleep(0.2)
    
    def _auto_copy_response(delay):
        w, h = _get_monitor_size()
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

        print(pyperclip.paste())


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


    if not _is_browser_running("chrome"):
        print("_is_browser_running")
        _open_browser()
        _auto_prompt(prompt)
    else:
        print("not _is_browser_running")
        _auto_prompt(prompt)

if __name__ == "__main__":
    rang = Rang(('A', 1), ('B', 1))
    g_p = generate_prompt("English", "Shabu", 3, rang, 2)
    prompt = _parse_formatted_prompt(g_p)
    time.sleep(1)
    automate_browser(prompt)     
