from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()
