from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datainsert

wd = webdriver.Chrome()

def scrape(sheet, link):

    wd.get(link)

    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    upscroll = time.time()
    
    while True:
        wd.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

        initialScroll = finalScroll
        finalScroll += 3000
    
        time.sleep(1)
    
        end = time.time()

        if round(end - upscroll) > 3:
            print("Scroll up")
            wd.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            upscroll = time.time()

        try:
            wd.find_element(By.XPATH, '//button[@data-tracking-control-name="infinite-scroller_show-more"]').click()
        except:
            pass
    
        if round(end - start) > 60:
            break

    job = wd.find_elements(By.XPATH, '//div[@class="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card"]')

    listjobs = []


    for x in job:
        job_name = x.find_element(By.CLASS_NAME, "base-search-card__title").get_attribute("innerText")
        job_company = x.find_element(By.CLASS_NAME, "hidden-nested-link").get_attribute("innerText")
        job_location = x.find_element(By.CLASS_NAME, "job-search-card__location").get_attribute("innerText")
        job_link = x.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")

        listjobs.append((job_name, job_company, job_location, job_link))

    datainsert.datainsert(listjobs, f"{sheet}!")


