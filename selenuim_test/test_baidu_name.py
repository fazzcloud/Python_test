#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：利用name定位

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.find_element_by_name("wd").send_keys("ceshi")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[2]/input").click()
    time.sleep(3)
    print("test pass,element found name !")
except  Exception as error:
    print("test fail,%s"%(error))

driver.quit()