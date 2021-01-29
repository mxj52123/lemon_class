from commen import method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
url = test_data.dict1.get("url")
username = test_data.dict1.get("username")
password = test_data.dict1.get("password")
key = test_data.dict1.get("key")
num = method.search_fun(driver, url, username, password, key)
if key in num:
    print("结果搜索成功，测试通过")
else:
    print("测试不通过")

