from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
chrome_options.add_argument('--disable-web-security')
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--allow-running-insecure-content')

profiles = range(1,2)

desired_category_vote = {
    "Best Solo Artist" : "Louis Tomlinson",
    "Fandom of the Year" : "Louies (Louis Tomlinson)",
    "Best Group" : "One Direction",
    "Most Anticipated Album of 2022" : "'TBA' - Louis Tomlinson"
}
title = "United By Pop Awards 2021"

categories = desired_category_vote.keys()
votes = desired_category_vote.values()

for p in profiles:
    try:
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
        driver.get('https://www.unitedbypop.com/music/fandoms/united-by-pop-awards-2021/')
        WebDriverWait(driver, 10).until(
            expected_conditions.title_contains(title))
        try:
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "pmc-atlasmg-adhesion-bar")))
            driver.find_element_by_id("pmc-atlasmg-adhesion-bar").find_element_by_id("pmc-atlasmg-adhesion-close").click()
        except:
            pass

        for q in driver.find_elements_by_css_selector('.CSS_Poll.PDS_Poll'):
            if q.find_element_by_css_selector('.css-question-top.pds-question-top').find_element_by_tag_name('div').text not in categories:
                continue
            for va in list(a for a in q.find_elements_by_css_selector('.css-answer-row.pds-answer-row')):
                if va.text not in votes:
                    continue
                WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'input')))
                va.find_element_by_tag_name("input").click()
                WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.css-vote-button.pds-vote-button')))
                q.find_element_by_css_selector('.css-vote.pds-vote').find_element_by_css_selector('.css-vote-button.pds-vote-button').click()
        sleep(5)
    except:
        print("ERROR")
        pass
    else:
         driver.quit()
    finally:
        driver.quit()
