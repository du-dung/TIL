from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get(
    "https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%ED%99%A9%EC%B9%98%EC%97%B4+%EA%B7%BC%EC%9C%A1")  # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'imgs_homework/{i}.jpg')
    i += 1

driver.quit()  # 끝나면 닫아주기
