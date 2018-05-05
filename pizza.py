
import codecs

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()

'''
driver.get('https://pizzahut.jp/pc/top')
driver.implicitly_wait(5)

driver.find_element_by_class_name("spm-dialog-close").click()


driver.find_element_by_id("id2").click()
driver.find_element_by_id("id28").send_keys("wasedakaisei@gmail.com")
driver.find_element_by_id("id29").send_keys("bemyself1111")
driver.find_element_by_id("id2b").click()
driver.get("https://pizzahut.jp/pc/set_menu/?link_id=chd_set")

html_source = driver.page_source # アクセスしたサイトのページソースを返す
bs_obj = BeautifulSoup(html_source) # ページソースを引数にとり、BeautifulSoupのオブジェクトを生成
'''

driver.get('https://pizzahut.jp/pc/set_menu/')
html_source = driver.page_source # アクセスしたサイトのページソースを返す
bs_obj = BeautifulSoup(html_source) # ページソースを引数にとり、BeautifulSoupのオブジェクトを生成

print(html_source)
