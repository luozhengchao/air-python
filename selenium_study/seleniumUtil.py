from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


# 获取selenium驱动
def get_driver():
    options = Options()
    # options.add_argument('--headless')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(chrome_options=options, executable_path='./plugin/chromedriver')
    return driver
