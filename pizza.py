

import codecs

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error

def cmp(a, b):
    if a == b: return 0
    return -1 if a < b else 1

def getpizzalist():

    price=[]
    p=[]

    html_source = urllib.request.urlopen("https://pizzahut.jp/pc/set_menu/")
    soup = BeautifulSoup(html_source,"html.parser") # ページソースを引数にとり、BeautifulSoupのオブジェクトを生成
    i=0

    pizzalist=soup.find_all("p",class_="ph3_title")
    pizzaprice=soup.find_all("ul",class_="ph3_list-size")
    pizzalink=soup.find_all("li",class_="ph3_btn ph3_red ph3_small ph3_w-100")

    for name in pizzalist:
        text=re.sub(r'[\t\n]',"",name.text,flags=re.MULTILINE)
        text=text.replace("\u3000"," ")
        p.append({"name":text})
    for pprice in pizzaprice:
        text=re.sub(r'[\t\n]',"",pprice.text,flags=re.MULTILINE)
        text=text.replace("\u3000"," ")
        p[i]["size"]=re.search(r"S|M|L",text).group()
        p[i]["price"]=int(re.search(r"[\d,]+",text).group().replace(",",""))
        i+=1

    s=sorted(p,key=lambda x:x["price"])
    return s;



if __name__ == '__main__':

    p=[]
    pizza=[]
    price=[]
    html_source = urllib.request.urlopen("https://pizzahut.jp/pc/set_menu/")
    soup = BeautifulSoup(html_source,"html.parser")
    i=0

    pizzalist=soup.find_all("p",class_="ph3_title")
    pizzaprice=soup.find_all("ul",class_="ph3_list-size")
    pizzalink=soup.find_all("li",class_="ph3_ta-c")

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
    for i in range(0,len(pizzalink)-1):
        p[i]["link"]=pizzalink[i].a.get("href").replace("..","https://pizzahut.jp/pc");

#    print(pizzalink)

    p=sorted(p,key=lambda x:x["price"])
    #print(p)



    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(p[1]["link"])

    driver.find_element_by_class_name("ph3_header-btn").click()
    driver.implicitly_wait(1)

    driver.find_element_by_css_selector('input[name="shopUnSelectedContainer:orderStartLink:modal:content:item:form:emailText"]').send_keys("wasedakaisei@gmail.com")
    driver.find_element_by_css_selector('input[name="shopUnSelectedContainer:orderStartLink:modal:content:item:form:passwordText"]').send_keys("bemyself1111")
    driver.find_element_by_css_selector('a[class="ph3_btn ph3_red ph3_small"]').click()
    driver.find_element_by_css_selector('a[data-ph3_name="enabledDetermineLink"]').click()


    driver.implicitly_wait(5)
    driver.execute_script(driver.find_element_by_css_selector('a[class="ph3_btn ph3_red ph3_middle ph3_sp-w-100"]').get_attribute("onclick"))

    driver.execute_script(driver.find_element_by_css_selector('a[class="ph3_btn ph3_red ph3_large ph3_btn-w-fix"]').get_attribute("onclick"))
    try:
        driver.execute_script("PH.SideRecommendModal.closeSideRecommendModal(this)")
    except Exception as e:
        raise

    '''
    print(driver.find_element_by_css_selector('li a').get_attribute("onclick"))

    driver.implicitly_wait(5)
    driver.get('https://pizzahut.jp/pc/set_menu/')

    driver.get(p[0]["link"])

    driver.get("https://pizzahut.jp/pc/set_menu/?link_id=chd_set")

    html_source = driver.page_source # アクセスしたサイトのページソースを返す
    bs_obj = BeautifulSoup(html_source) # ページソースを引数にとり、BeautifulSoupのオブジェクトを生成

    driver.get('https://pizzahut.jp/pc/set_menu/')
    html_source = driver.page_source # アクセスしたサイトのページソースを返す
    driver.quit()
    '''
