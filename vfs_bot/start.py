from csv import excel
import time
import undetected_chromedriver as uc
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# DISABLE HERE options.add_argument("--headless")  # Run in headless mode
options.add_argument("--user-data-dir=/home/efe/.config/google-chrome/")  # Use your Chrome profile
options.add_argument("--profile-directory=Default")  # Specify the exact profile

#driver = webdriver.Chrome(options=options)
driver = uc.Chrome(headless=False,use_subprocess=False)

#driver_path = "/home/efe/Desktop/Projects/chromedriver-linux64/chromedriver"
#driver_path = "/usr/bin/google-chrome"
#browser = webdriver.Chrome(executable_path=driver_path)
#browser = webdriver.Chrome()

def login():
    """
    uname = driver.find_element_by_xpath("//input[@id='mat-input-0']")
    uname.send_keys(vfs_email_address)
    pwd = driver.find_element_by_xpath("//input[@id='mat-input-1']")
    pwd.send_keys(vfs_account_password)
    sign_in_button = driver.find_element_by_xpath("//button/span")
    sign_in_button.click()
    time.sleep(10)
    """
    driver.get('https://visa.vfsglobal.com/tur/tr/fra/login')
    time.sleep(15)
    print("sleep done")
    try:
       cooke_button = driver.find_element(By.XPATH, '//button[@id="onetrust-reject-all-handler"]')
       cooke_button.click()
       print("Clicked no cookie")
    except:
       print("Cookie button not found")
    # $x('//*[@type="checkbox"]')
    try:
        my_checkbox = driver.find_element(By.XPATH, '//*[@type="checkbox"]')
        my_checkbox.click()
        print("CF found")
    except:
        print("CF button not found")

    # Click on the checkbox (this will check/uncheck it) # mat-mdc-button-touch-target
    # # $x('//*[@="mat-mdc-button-touch-target"]')
    # $x('//*[@class="mat-mdc-button-touch-target"]')


    time.sleep(30)
    try:
        mail = driver.find_element(By.XPATH, '//*[@id="email"]')
        mail.send_keys('efeayseli@gmail.com')
    except:
        print("No mail element?")

    xpaths = [
        '//input[@id="mat-input-0"]',
        '//input[@id="mat-input-4"]',
        '//*[@id="password"]'
    ]

    for i in xpaths:
        print(i)
        try:
            pw = driver.find_element(By.XPATH, i)
            print("Element found for XPath: "+str(i))
            pw.click()
            time.sleep(5)
        except:
            print("Element not found for XPath: "+str(i))

    time.sleep(10)


    #pw = driver.find_element(By.XPATH, '//input[@id="mat-input-0"]')
    #pw = driver.find_element(By.XPATH, '//input[@id="mat-input-4"]')
    #pw = driver.find_element(By.XPATH, '//*[@id="password"]')


    #mail = browser.find_element_by_xpath(xe)
    #pw = browser.find_element_by_xpath(xpw)

    my_pass = 'Individual12**' # {shift} {numeric} -> {symbolic}
    my_pass = ["{shift}", "I", "{shift}", "n", "d", "i", "v", "i", "d", "u", "a", "l", "{numeric}", "1", "2", "{symbolic}", "*", "*"]

    for i in my_pass:
        try:
            print("//button[@name=\'"+str(i)+"\']")
            my_button_id = "//button[@name=\'"+str(i)+"\']"
            button = driver.find_element(By.XPATH, my_button_id)
            button.click()
            time.sleep(0.2)  # Delay to simulate natural typing
        except:
            print("Button: "+str(i)+" not found")
    """
        if char in button_names:
            try:
                button = driver.find_element(By.XPATH, f"//button[@name='{char}']")
                button.click()
                time.sleep(0.2)  # Delay to simulate natural typing
            except:
                print(f"Button '{char}' not found!")
    """
    print("All typed sleeping for button")
    #justify-content-center ng-star-inserted
    empty_place = driver.find_element(By.XPATH, '//*[@class="ustify-content-center ng-star-inserted"]')
    empty_place.click()
    time.sleep(10)
    pass_button = driver.find_element(By.XPATH, '//*[@class="mat-mdc-button-touch-target"]')
    pass_button.click()
    time.sleep(40)
    print(driver.title)
    #appointment(xpaths.appointment,xpaths.selone)

def appointment(ax,sx):
    browser.find_element_by_xpath(ax).click()
    time.sleep(random.randint(3,5))
    selelement = Select(browser.find_element_by_xpath(sx))
    while True:
        #selelement.select_by_visible_text('Poland Visa Application Center - Ankara')
        selelement.select_by_visible_text('Poland Visa Application Center-Altunizade')
        time.sleep(random.randint(3,5))
        selelement.select_by_visible_text('Poland Visa Application Center-Altunizade')
        time.sleep(random.randint(3,5))
        browser.find_element_by_xpath(ax).click()
        time.sleep(10)



login()
