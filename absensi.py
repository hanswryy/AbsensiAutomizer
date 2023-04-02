from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

jadwal = {
    "1" : ["INFORMATIKA", "BHS.SUNDA", "PEND.AGAMA"],
    "2" : ["BHS.INDONESIA", "PENJASORKER", "MATEMATIKA WAJIB", "BHS.INGGRIS WAJIB"],
    "3" : ["PPKN", "FISIKA", "SEJARAH INDONESIA", "SENI BUDAYA"],
    "4" : ["KIMIA", "PKWU", "BIOLOGI", "BHS.INGGRIS MINAT"],
    "5" : ["MATEMATIKA MINAT"]
}

date = datetime.datetime.now()
today = datetime.date.today()

browser = webdriver.Edge("C:/Users/Hans/Documents/msedgedriver.exe")
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSe5_-hMal5BiXOASF5HKTPN-myhmEr9rDiZvgMbziHHG3lbbQ/viewform')
browser.implicitly_wait(10)

time.sleep(1)

ask = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
ask.send_keys("Farhan Muhammad Luthfi")

browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]').click()
ask = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[8]')

try:
    while ask.is_selected() is False:
        ask.click()
except:
    pass

browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('13')
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('farhan.hans257@gmail.com')
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(today.strftime('%d-%m-%Y'))
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(date.strftime('%H'))
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys(date.strftime('%M'))

jam = date.strftime('%H')
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(jadwal[date.strftime('%w')][int(int(jam)/2) - 3])
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()

time.sleep(2)

browser.quit()