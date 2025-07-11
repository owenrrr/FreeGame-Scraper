import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import shutil
import os

COLOR_YELLOW="\033[1;33m"
COLOR_GREEN="\033[1;32m"
COLOR_RESET="\033[0m"

# Modify this
# If you're not certain, go to any website and examine by:
# Open developer tools > Networks > Check any http request > View headers > Find user-agent
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36" 

uc.Chrome.__del__ = lambda self: None

def print_divider(char='-', padding=0):
    width = shutil.get_terminal_size().columns
    line = char * (width - padding)
    print(COLOR_GREEN,line[:-1],COLOR_RESET)

def fetch():
    url = "https://steamdb.info/upcoming/free/"

    options = uc.ChromeOptions()
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

    driver = uc.Chrome(options=options)  
    try:
        driver.get(url)
        for i in range(10):
            cookies = driver.get_cookies()
            cf_clearance_cookie = next((c['value'] for c in cookies if c['name'] == 'cf_clearance'), None)
            if cf_clearance_cookie:
                fetch_games(cf_clearance=cf_clearance_cookie)
                break
            time.sleep(1)
    except Exception:
        pass
    finally:
        try:
            driver.quit()
        except Exception:
            pass
        del driver  

def fetch_games(cf_clearance):
    with sync_playwright() as p:
        with p.chromium.launch(headless=True) as browser:  
            context = browser.new_context(user_agent=USER_AGENT)
            context.add_cookies([
                {
                    "name": "cf_clearance",
                    "value": cf_clearance,
                    "domain": "steamdb.info",
                    "path": "/",
                    "httpOnly": True,
                    "secure": True
                }
            ])

            page = context.new_page()
            page.goto("https://steamdb.info/upcoming/free/", wait_until="load")  
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")

            game_names = []
            for h4 in soup.select("h4.panel-sale-name"):
                a_tag = h4.find("a")
                if a_tag:
                    game_name = a_tag.get_text(strip=True)
                    game_names.append(game_name)

            print_divider()
            for name in game_names[1:]:
                print(COLOR_YELLOW, "> ", name, COLOR_RESET)
            print_divider()

if __name__ == "__main__":
    fetch()
    os._exit(0)