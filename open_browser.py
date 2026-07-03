import psutil
import webbrowser
import pyautogui
import pyperclip #for copying to clipboard
import time

from playwright.sync_api import sync_playwright

from generate_prompt import Range, generate_prompt, _parse_formatted_prompt
BROWSERS = {
    "chrome": ["chrome.exe", "google-chrome", "chrome"],
    "firefox": ["firefox.exe", "firefox"],
    "edge": ["msedge.exe", "msedge"],
    "opera": ["opera.exe", "opera"],
    "brave": ["brave.exe", "brave"],
}

def is_browser_running(browser):
    names = BROWSERS.get(browser.lower(), [])
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() in names:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Creates a new incognito context
        context = browser.new_context()

        # Page inside the incognito context
        page = context.new_page()

        page.goto("https://chatgpt.com")
       
"""
if not is_browser_running("chrome"):
    webbrowser.open("https://www.google.com")
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    #pyautogui.write("https://chatgpt.com/")
    #pyautogui.press('enter')
    time.sleep(1)
    range = Range(('A', 1), ('B', 1))
    g_p = generate_prompt("English", "Shabu", 3, range, 2)
    prompt = _parse_formatted_prompt(g_p)
    time.sleep(1)
    pyperclip.copy(prompt)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(3)
    pyautogui.press('enter')
"""



"""
Option 2: Open the browser if it's not running
import webbrowser

if not is_browser_running("chrome"):
    webbrowser.open("https://www.google.com")

Option 3: Launch a specific browser

import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([chrome_path])

subprocess.Popen([chrome_path, "https://www.google.com"])

Option 4: Cross-platform launching

import shutil
import subprocess

chrome = shutil.which("google-chrome") or shutil.which("chrome")

if chrome:
    subprocess.Popen([chrome])

Option 5: Check if Chrome is already running with remote debugging

import requests

try:
    r = requests.get("http://127.0.0.1:9222/json/version", timeout=1)
    print("Chrome debugging is available")
except requests.exceptions.RequestException:
    print("Chrome debugging is not running")


    
Putting it together
import psutil
import subprocess
import os

def ensure_chrome_running():
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] and proc.info["name"].lower() == "chrome.exe":
            print("Chrome is already running.")
            return

    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(chrome):
        subprocess.Popen([chrome])
        print("Chrome started.")
    else:
        print("Chrome is not installed.")

ensure_chrome_running()
"""

"""
import pyautogui

pyautogui.hotkey('ctrl', 'shift', 'n')
"""