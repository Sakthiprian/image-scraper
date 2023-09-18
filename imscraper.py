import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

keywords = [
    "Flipkart boxes",
    "Cardboard boxes",
    "Flipkart parcel box",
    "Cardboard box",
    "Flipkart package",
    "Shipping boxes",
    "Corrugated boxes",
    "Custom printed boxes",
    "Storage boxes",
    "Moving boxes",
    "Packaging boxes",
    "Brown boxes",
    "White boxes",
    "Gift boxes",
    "Jewelry boxes",
    "Pizza boxes",
    "Shoe boxes",
    "Cake boxes",
    "Amazon boxes",
    "Postal boxes"
]
def imscrape(keyword_list,folder_name):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    url = "https://www.google.com/search?client=firefox-b-d&sca_esv=566290925&sxsrf=AM9HkKmoM8_ByTXhnFK0z18dGBkdOwniHQ:1695048610872&q={s}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjIys-StLSBAxWQwjgGHQHWAAsQ0pQJegQIDBAB&biw=1440&bih=665&dpr=1.33"

    for j, keyword in enumerate(keywords):
        driver.get(url.format(s=keyword))

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

        imgResults = driver.find_elements(By.XPATH, "//img[contains(@class,'rg_i Q4LuWd')]")

        src = []
        for img in imgResults:
            src.append(img.get_attribute('src'))

        count = 0  # Move count outside the inner loop

        for i, img_url in enumerate(src):
            try:
                if img_url and img_url.startswith('http'):
                    img_filename = f"{keyword.replace(' ', '_')}_{count}.jpg"
                    urllib.request.urlretrieve(img_url, os.path.join(folder_name, img_filename))
                    count += 1
            except Exception as e:
                print(f"Error downloading image {i} for keyword {keyword}: {str(e)}")

    driver.quit()

imscrape(keywords,"train_data")
