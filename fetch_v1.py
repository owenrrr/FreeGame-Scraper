import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import shutil
import os

COLOR_YELLOW="\033[1;33m"
COLOR_GREEN="\033[1;32m"
COLOR_RESET="\033[0m"

uc.Chrome.__del__ = lambda self: None

def print_results(results: list, char='-', padding=0):
    width = shutil.get_terminal_size().columns
    line = char * (width - padding)
    print(COLOR_GREEN,line,COLOR_RESET)
    for result in results[1:]:
        print(COLOR_YELLOW, "> ", result, COLOR_RESET)
    print(COLOR_GREEN,line,COLOR_RESET)
        
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
                HTML = driver.page_source
                extract(HTML=HTML)
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
        
def extract(HTML):
    soup = BeautifulSoup(HTML, "html.parser")
    game_names = []
    for h4 in soup.select("h4.panel-sale-name"):
        a_tag = h4.find("a")
        if a_tag:
            game_name = a_tag.get_text(strip=True)
            game_names.append(game_name)
    print_results(results=game_names)

if __name__ == "__main__":
    fetch()
    os._exit(0)