# 封装打开浏览器的函数
import time
def open_url(driver, url):
    driver.get(url)
    driver.maximize_window()
# 封装登陆函数
def login_fun(driver, username, password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath('//input[@id="rememberUserCode"]/following-sibling::ins').click()
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(2)
# 封装搜索函数
def search_fun(driver,url,username,password, key):
    open_url(driver, url)
    login_fun(driver, username, password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    # 找到单据编号输入，必须先找到iframe的id
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    id_frame = id+"-frame"
    # print(id)
    # driver.switch_to.frame(id_frame)  # 找到frameid，进入到子页面
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))  # 通过元素定位切换到子页面
    driver.find_element_by_id("searchNumber").send_keys(key)  # 搜索框输入
    driver.find_element_by_xpath("//a[@id='searchBtn']/span/span").click()   # 点击搜索
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
