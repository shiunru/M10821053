from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.dcard.tw/f'
driver.get(url)

inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('python')

driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)

html = driver.page_source
soup =bs(html, 'html.parser')

data = soup.find_all('span',{'class': 'sc-6oxm01-2 hiTIMq'})

meta_datas = []
for i in data:
    meta_datas.append(i.text)
print(meta_datas)

forums = []
author = []
times = []
for i in range(len(meta_datas)):
    if i % 3 == 0:
        forums.append(meta_datas[i])
    if i % 3 == 1:
        author.append(meta_datas[i])
    if i % 3 == 2:
        times.append(meta_datas[i])

titles =[]
for i in soup.find_all('h2',{'class':'sc-1v1d5rx-3 eihOFJ'}):
    titles.append(i.text)
print(titles)

hrefs = []
for i in soup.find_all('a',{'class':'sc-1v1d5rx-4 gCVegi'}):
    hrefs.append(i['href'])

links = []
for href in hrefs:
    links.append(urljoin(url,href))
print(links)

for i in range(len(forums)):
    print(forums[i], titles[i], links[i])
