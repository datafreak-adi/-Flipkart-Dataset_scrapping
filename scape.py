from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


##Importing webdriverwait to initiate wait time until next page loaded

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



s = Service("C:/Users/ADITYA/OneDrive/Desktop/chromedriver.exe")


# set different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# to remove errors
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

#maximize the browser
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=chrome_options)
wait = WebDriverWait(driver, 10)



#site opening
driver.get("https://www.flipkart.com/search?q=smartphones&page=1")
time.sleep(2)


#Filtering
driver.find_element(by=By.XPATH, value="//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[4]/div/label/div[2]").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@id='container']/div/div[3]/div/div[2]/div[26]/div/div/nav/a[11]/span").click()
time.sleep(2)

#save html of all pages
with open("flipkart.html", "w", encoding="utf-8") as f:
    while True:
        # Get and save the HTML of the current page
        html = driver.page_source
        f.write(html)
        f.write("\n\n<!-- PAGE BREAK -->\n\n")  # Optional: add a marker for page breaks

        # Store the current URL
        current_url = driver.current_url

        # Click on the "Next" button
        next_button_xpath = "//*[@id='container']/div/div[3]/div/div[2]/div[26]/div/div/nav/a[12]/span"
        alternate_next_button_xpath = "//*[@id='container']/div/div[3]/div/div[2]/div[2]/div/div/nav/a[12]/span"

        try:
            # Use WebDriverWait to wait for the "Next" button to be clickable
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            next_button.click()
            print("Successfully navigated to the next page.")
            time.sleep(2)  # Wait for the page to load
        except Exception as e:
            print("Trying alternate XPath due to exception or last page reached.")
            try:
                # Attempt using the alternate XPath
                next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, alternate_next_button_xpath)))
                next_button.click()
                print("Successfully navigated to the next page using alternate XPath.")
                time.sleep(2)
            except Exception as e:
                print(f"Error or last page reached: {e}")
                break

        # Get the new URL
        new_url = driver.current_url

        # If the URL hasn't changed, break the loop as it indicates the last page
        if new_url == current_url:
            print("Detected the last page; URL did not change.")
            break












