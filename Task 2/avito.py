from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = "#app > div > div.index-root-k1Ib4.index-responsive-aOpFS.index-page_default-_b5bD > div:nth-child(1) > div > div.style-item-view-PCYlM > div.style-item-view-content-SDgKX > div.style-item-view-content-left-bb5Ih > div.js-item-view-title-info > div > div.style-title-info-actions-NEXbl > div > div > div > div.style-header-add-favorite-M7nA2 > button"
LINK = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"

try:

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get(LINK)

    button = browser.find_element(By.CSS_SELECTOR, PATH)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
