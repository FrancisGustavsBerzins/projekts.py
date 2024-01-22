import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def setup_driver():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def navigate_to_page(driver, url):
    driver.get(url)
    time.sleep(2)

def click_element_by_id(driver, element_id):
    element = driver.find_element(By.ID, element_id)
    element.click()
    time.sleep(2)

def scrape_data(driver):
    nosaukums = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
    ražotājs = driver.find_elements(By.XPATH, '//tbody/tr/td[4]')
    stavoklis = driver.find_elements(By.XPATH, '//tbody/tr/td[6]')
    cena = driver.find_elements(By.XPATH, '//tbody/tr/td[7]')

    ražotājs_result = []

    min_len = min(len(nosaukums), len(ražotājs), len(stavoklis), len(cena))

    for i in range(min_len):
        data = {
            "nosaukums": nosaukums[i].text if i < len(nosaukums) else None,
            "ražotājs": ražotājs[i].text if i < len(ražotājs) else None,
            "stavoklis": stavoklis[i].text if i < len(stavoklis) else None,
            "cena": cena[i].text if i < len(cena) else None
        }
        ražotājs_result.append(data)

    return ražotājs_result


def save_to_excel(data, filename="projekts.xlsx"):
    df_data = pd.DataFrame(data)
    df_data.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    driver = setup_driver()

    try:
        navigate_to_page(driver, "https://www.ss.lv/")
        click_element_by_id(driver, "mtd_293")
        click_element_by_id(driver, "ahc_13285")

        scraped_data = scrape_data(driver)
        save_to_excel(scraped_data)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()