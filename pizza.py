

import codecs

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error

def cmp(a, b):
    if a == b: return 0
    return -1 if a < b else 1

'''

driver = webdriver.Chrome()
driver.maximize_window()

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

pizza=[]
price=[]
p=[]
'''
driver.get('https://pizzahut.jp/pc/set_menu/')
html_source = driver.page_source # アクセスしたサイトのページソースを返す
driver.quit()
'''
html_source = urllib.request.urlopen("https://pizzahut.jp/pc/set_menu/")
soup = BeautifulSoup(html_source,"html.parser") # ページソースを引数にとり、BeautifulSoupのオブジェクトを生成
i=0

pizzalist=soup.find_all("p",class_="ph3_title")
pizzaprice=soup.find_all("ul",class_="ph3_list-size")
#print(pizzalist)
for name in pizzalist:
    text=re.sub(r'[\t\n]',"",name.text,flags=re.MULTILINE)
    text=text.replace("\u3000"," ")
    pizza.append(text)
    p.append({"name":text})
for pprice in pizzaprice:
    text=re.sub(r'[\t\n]',"",pprice.text,flags=re.MULTILINE)
    text=text.replace("\u3000"," ")
    #price.append(text)
    p[i]["size"]=re.search(r"S|M|L",text).group()
    p[i]["price"]=int(re.search(r"[\d,]+",text).group().replace(",",""))
    i+=1
#print(pizza)
#print(price)
print(p)

s=sorted(p,key=lambda x:x["price"])
print("\n")
print(s)
