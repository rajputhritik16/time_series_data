from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

driver= webdriver.Chrome(service=Service("F:/us_based_data/src/utils/chromedriver.exe"))
url= "https://apps.bea.gov/iTable/?reqid=19&step=3&isuri=1&1921=survey&1903=239"
driver.get(url)

df= pd.DataFrame()

while True:
    try:
        navigate= driver.find_element(By.CLASS_NAME, "nav-link active").click()
        form_bar= driver.find_element(By.CLASS_NAME, "form-control").click()
        categories= driver.find_element(By.TAG_NAME, "option")
        for c in categories:
            c.click()
            links= driver.find_elements(By.CLASS_NAME, "card-header pointable text-uppercase")
            for l in links:
                table_name= (l.text).strip()
                l.click()
                internal_links= driver.find_element(By.CLASS_NAME, "list-group-item btn-sm pointable px-5 py-2 mt-1 border border-right-0 border-top-0 border-left-0")
                for il in internal_links:
                    il.click()
                    table = driver.find_element(By.CSS_SELECTOR, 'table')
                    df = pd.read_html(table.get_attribute('outerHTML'))
                    df.to_csv(table_name+".csv")
    except:
        pass
        



