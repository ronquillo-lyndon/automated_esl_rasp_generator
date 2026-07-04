# import psutil
# import webbrowser
import pyautogui
import pyperclip #for copying to clipboard
import time

from generate_prompt import Range, generate_prompt, _parse_formatted_prompt

from playwright.sync_api import sync_playwright

def browser(prompt):
    with sync_playwright() as p:
        #Open new page without acc
        browser = p.chromium.launch(headless=False)
        
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://chatgpt.com/")

        def _close_browser():
            browser.close()
        def _close_context():
            context.close()
        
        def _close_browser_and_context():
            _close_browser()
            _close_context
        
        #copy paste
        pyperclip.copy(prompt)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        pyautogui.press('enter')

        input("Browser is open. Press Enter to close...")
        

if __name__ == "__main__":
    range = Range(('A', 1), ('B', 1))
    g_p = generate_prompt("English", "Shabu", 3, range, 2)
    prompt = _parse_formatted_prompt(g_p)
    time.sleep(1)
    browser(prompt)     
