import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_service = Service("c:\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.digikala.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='دسته‌بندی کالاها']").click()
driver.find_element(By.XPATH, "//p[text()='موبایل']").click()
time.sleep(1)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/div[1]/div[1]/input[1]").send_keys(
    "samsung")
driver.find_element(By.XPATH,
                    "//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='محدوده قیمت']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='min']").send_keys("10000000")
driver.find_element(By.CSS_SELECTOR, "input[name='max']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='max']").send_keys("20000000")
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[3]/div[2]/section[1]/div[2]/div[1]/a[1]/div[1]/article[1]").click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='افزودن به سبد']").click()
driver.find_element(By.XPATH, "//div[text()='فعلا تمایل ندارم']").click()
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]").click()
