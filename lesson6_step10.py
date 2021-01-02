from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math




try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    buttonBook = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    buttonBook.click()

    numX = browser.find_element_by_id("input_value").text
    answerFunc = math.log(abs(12*math.sin(int(numX))))
    input = browser.find_element_by_id("answer")
    input.send_keys(str(answerFunc))

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




