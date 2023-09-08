from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

CHROMEDRIVER_PATH = r"D:\Program Files (x86)\chromedriver-win64\chromedriver.exe"

# Créez une nouvelle instance du driver Chrome
# executable_path est faculatatif si chromedriver est référencé par le PATH
driver_service = Service(executable_path=CHROMEDRIVER_PATH)
driver_options = webdriver.ChromeOptions()

with webdriver.Chrome(service=driver_service, options=driver_options) as driver:
    # Accédez à la page souhaitée
    driver.get("https://www.google.com/")

    # Trouvez le bouton "J'ai de la chance" et cliquez dessus (pour la version anglaise)
    # Notez que le bouton peut avoir un nom différent selon la langue de votre navigateur
    accept_all = driver.find_element(By.XPATH, "//button/div[contains(text(),'Accept all')]")
    accept_all.click()

    lucky_button = driver.find_element(By.XPATH, "//input[@id='gbqfbb' and @value=\"I'm Feeling Lucky\"]")
    lucky_button.click()

    time.sleep(2)

    page_source = driver.page_source
    print(page_source)

    # Fermez le navigateur
    driver.close()