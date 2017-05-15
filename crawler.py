# dependency for Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

# Dependency for wait element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dependancy for other element
import urllib
import time
import pickle
import string
import os


start_time = time.time()

# Cookie saver


def save_cookies(driver, file_path):
    LINE = "{domain} False {path} {secure} {expiry} {name} {value}\n"
    with open(file_path, 'w') as file:
        for cookie in driver.get_cookies():
            file.write(
                LINE.format(
                    **cookie))


def load_cookies(driver, file_path):
    with open(file_path, 'r') as file:
        driver.execute_script(
            file.read())

# Bot crawler


def crawler_wannacrypt():

    afficheur = Display(visible=0, size=(850, 600))
    afficheur.start()

    navigateur = webdriver.Firefox()
    url_list = ["https://intel.malwaretech.com/botnet/wcrypt/?t=1m&bid=all", "https://intel.malwaretech.com/botnet/wcrypt/?t=5m&bid=all", 
                "https://intel.malwaretech.com/botnet/wcrypt/?t=30m&bid=all", "https://intel.malwaretech.com/botnet/wcrypt/?t=1h&bid=all",
                "https://intel.malwaretech.com/botnet/wcrypt/?t=24h&bid=all"]
    
    for url in url_list:
        navigateur.get(url)
   
        navigationStart = navigateur.execute_script(
            "return window.performance.timing.navigationStart")
        responseStart = navigateur.execute_script(
            "return window.performance.timing.responseStart")
        domComplete = navigateur.execute_script(
            "return window.performance.timing.domComplete")

        backendPerformance = responseStart - \
            navigationStart
        frontendPerformance = domComplete - \
            responseStart

        getwanna_online = WebDriverWait(navigateur, 12).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-4']/div/div")))
        if "1m" in url:
            print(getwanna_online.get_attribute("innerHTML") + " in 1 minutes")
        if "5m" in url:
            print(getwanna_online.get_attribute("innerHTML") + " in 5 minutes")
        if "30m" in url:
            print(getwanna_online.get_attribute("innerHTML") + " in 30 minutes")
        if "1h" in url:
            print(getwanna_online.get_attribute("innerHTML") + " in 1 heures")
        if "24h" in url:
            print(getwanna_online.get_attribute("innerHTML") + " in 24 heures")

    print("")
    print("Terminer.")

    print(
        "Back End: %s ms" %
        backendPerformance)
    print(
        "Front End: %s ms" %
        frontendPerformance)
    navigateur.close()
    navigateur.quit()


crawler_wannacrypt()

interval = time.time() - start_time
print('Total time in seconds:',interval)
exit(1)

