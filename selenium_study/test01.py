import selenium_study.seleniumUtil as su

driver = su.get_driver()


# 模拟在浏览器中输入搜索B并获取搜索结果
def test_search(driver):
    # 模拟浏览器
    driver.get('http://www.baidu.com')
    # 根据id找到百度的输入框
    input_element = driver.find_element_by_id('kw')
    # 模拟输入搜索内容
    input_element.send_keys("黑洞")
    # 根据id找到百度的确认按钮
    click_button = driver.find_element_by_id('su')
    # 模拟点击事件
    click_button.click()
    # 等5s
    driver.implicitly_wait(5)
    # 根据classname获取列表数据
    result_list = driver.find_elements_by_class_name('result')
    for result in result_list:
        print("列表标题：" + result.text)
        print("===========================================================================")


if __name__ == '__main__':
    test_search(driver)
