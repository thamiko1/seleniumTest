
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C:\\Users\\Thamiko\\OneDrive\\Desktop\\chromedriver.exe',options=options)
driver.get("https://referendum.2021.nat.gov.tw/pc/zh_TW/01/00000000000000000.html")

myDataSet = {
    '縣市':[],
    '行政區':[],
    '同意票數':[],
    '不同意票數':[],
    '有效票數':[],
    '無效票數':[],
    '投票數':[],
    '投票權人數':[],
    '已完成投票所投票率(%)':[],
    '有效同意票數對投票權人數(%)':[]

}

# #第17案
# search = driver.find_element('id','itemTextLink2')#17
# a = search.text
# # print(search.text)
# trt = driver.find_element(By.CLASS_NAME,'trT')
# # print(trt.text)
# trt2 = driver.find_element(By.XPATH,'//*[@id="divContent"]/table/tbody/tr[4]/td/table/tbody/tr[5]')
# # print(trt2.text)
# trt = trt.text.split()
# trt2 = trt2.text.split()
# myDataSet['縣市'].append(a)
# myDataSet['同意票數'].append(trt[0])
# myDataSet['不同意票數'].append(trt[1])
# myDataSet['有效票數'].append(trt[2])
# myDataSet['無效票數'].append(trt[3])
# myDataSet['投票數'].append(trt2[0])
# myDataSet['投票權人數'].append(trt2[1])
# myDataSet['已完成投票所投票率(%)'].append(trt2[2])
# myDataSet['有效同意票數對投票權人數(%)'].append(trt2[3])
# city = driver.find_element(By.LINK_TEXT,search.text)
# city.click()


# #臺北市
# search = driver.find_element('id','itemTextLink3')
# city = driver.find_element(By.LINK_TEXT,search.text).click()
# trt = driver.find_element(By.CLASS_NAME,'trT')
# print(trt.text)
# trt2 = driver.find_element(By.XPATH,'//*[@id="divContent"]/table/tbody/tr[4]/td/table/tbody/tr[5]')
# print(trt2.text)
b = ''
for i in range(2,393):#393
    search = driver.find_element('id',f'itemTextLink{i}')#17
    a = search.text
    city = driver.find_element(By.LINK_TEXT,search.text).click()
    # print(search.text)
    trt = driver.find_element(By.CLASS_NAME,'trT')
    # print(trt.text)
    trt2 = driver.find_element(By.XPATH,'//*[@id="divContent"]/table/tbody/tr[4]/td/table/tbody/tr[5]')
    # print(trt2.text)
    # print(a, trt.text, trt2.text)
    trt = trt.text.split()
    trt2 = trt2.text.split()
    
    if a[-1]=='縣' or a[-1]=='市' or i == 2:
        b = a
        a=''
        continue
    myDataSet['縣市'].append(b)
    myDataSet['行政區'].append(a)
    myDataSet['同意票數'].append(trt[0])
    myDataSet['不同意票數'].append(trt[1])
    myDataSet['有效票數'].append(trt[2])
    myDataSet['無效票數'].append(trt[3])
    myDataSet['投票數'].append(trt2[0])
    myDataSet['投票權人數'].append(trt2[1])
    myDataSet['已完成投票所投票率(%)'].append(trt2[2])
    myDataSet['有效同意票數對投票權人數(%)'].append(trt2[3])
    

# time.sleep(5)
driver.quit()

dataframe = pd.DataFrame(myDataSet)
print(dataframe)