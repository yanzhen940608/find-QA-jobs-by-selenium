from selenium import webdriver
from time import sleep


driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.indeed.com/")

driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys('QA Analyst')
# driver.find_element_by_xpath('//*[@id="text-input-where"]').send_keys('Montréal, QC')
driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()
n=1
lst=driver.find_elements_by_class_name('title')
for i in lst:
    i.find_element_by_tag_name('a').click()
    sleep(1)
    text=driver.find_element_by_id('vjs-content').text
    f=open("automation/requirements/req_%s.txt" % n,mode="w",encoding="utf-8")
    f.write(text)
    f.close()
    sleep(1)
    n+=1