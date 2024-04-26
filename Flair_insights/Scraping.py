from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.parispackagingweek.com/en/2022/10/31/next-generation-packaging-technologies-enabling-circularity-future-market-insights/'

driver = webdriver.Firefox()
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')

headings = soup.find_all('strong')

heading_texts = [heading.get_text(strip=True) for heading in headings]
img_tags = soup.find_all('img')

img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

links = [link['href'] for link in soup.find_all('a', href=True)]

v = pd.DataFrame({'Headings': [heading.get_text(strip=True) for heading in headings],
                  'Image URLs': img_urls[:len(headings)],  
                  'Links': links[:len(headings)]})  

v.to_excel('data.xlsx', index=False)

driver.quit()

