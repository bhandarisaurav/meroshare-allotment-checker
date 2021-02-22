import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.headless = True

GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_BIN


def get_allotted_stock_from_boid(boid_list=['1301090000394531', '1301090000382579']):
    boid_response = {}
    final_response = {}
    driver = None
    if(os.environ['APP_SETTINGS'] == "config.DevelopmentConfig"):
        driver = webdriver.Firefox(options=firefox_options)
    else:
        driver = webdriver.Chrome(
            CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get("https://www.sharesansar.com/ipo-result")
    boid_element = driver.find_element_by_id("boid")
    for boid in boid_list:
        boid_element.clear()
        boid_element.send_keys(boid)
        driver.find_element_by_id("searchipo").click()
        company_name = driver.find_element_by_id(
            "companyid").text.split("\n")[0]
        time.sleep(1)
        try:
            share_result = driver.find_element_by_css_selector(
                '#iporesult>div>table>tbody>tr>td:nth-child(4)')
            boid_response[boid] = share_result.text
        except:
            boid_response[boid] = "Not Alotted"
    driver.quit()
    final_response["company_name"] = company_name
    final_response["boid_results"] = boid_response
    print(final_response)
    return final_response


# get_allotted_stock_from_boid()
