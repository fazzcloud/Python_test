from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome()

driver.get("http://mynjwx.dashuhk.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[1]/uni-input/div/input").send_keys('黄蓓')
driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-input/div/input").send_keys('320106195910102024')
driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(13851493419)
driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[4]/uni-view[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[4]/uni-view[3]/uni-view/uni-view[2]/uni-scroll-view/div/div/div/uni-view/uni-view[2]/uni-picker-view/div/uni-picker-view-column[1]/div/div[3]/uni-view[5]/uni-view").click()
time.sleep(3)
#driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[4]/uni-view[3]/uni-view/uni-view[2]/uni-scroll-view/div/div/div/uni-view/uni-view[2]/uni-picker-view/div/uni-picker-view-column[2]/div/div[3]/uni-view[8]/uni-view").click()
#driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[4]/uni-view[3]/uni-view/uni-view[2]/uni-scroll-view/div/div/div/uni-view/uni-view[1]/uni-view[3]").click()
driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[5]/uni-input/div/input").send_keys('中保街130号1幢一单元201室')

