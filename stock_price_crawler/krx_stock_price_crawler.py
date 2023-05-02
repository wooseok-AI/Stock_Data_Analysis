from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()

url = "https://data.krx.co.kr/contents/MDC/MDI/outerLoader/index.cmd?screenId=MDCSTAT015&locale=ko_KR"

driver.get(url)

driver.find_element(By.XPATH, '//*[@id="MDCSTAT015_FORM"]/div[1]/div/table/tbody/tr[1]/td/label[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="jsSearchButton"]').click()
time.sleep(3)

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'CI-GRID-EVEN')))
time.sleep(1)

scroll = driver.find_element(By.CLASS_NAME, 'CI-FREEZE-SCROLLER')

stock_list = []

tr = 1
error_count = 0
for x in range(10000):
    stock_code = driver.find_element(By.XPATH,
                                         f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[1]').text

    if stock_code == '':
        error_count += 1
        print('에바양')
        if error_count == 10:
            break
        continue

    stock_name = driver.find_element(By.XPATH,
                                     f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[2]').text

    market_type = driver.find_element(By.XPATH,
                                      f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[3]').text
    belonging_department = driver.find_element(By.XPATH,
                                               f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[4]').text
    closing_price = driver.find_element(By.XPATH,
                                        f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[5]').text
    try:
        price_diff_img = driver.find_element(By.XPATH,
                                             f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[6]/img')
    except:
        plus_or_minus = ''

    price_diff = driver.find_element(By.XPATH,
                                     f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[6]').text
    percent_change = driver.find_element(By.XPATH,
                                         f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[7]').text
    opening_price = driver.find_element(By.XPATH,
                                        f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[8]').text
    high_price = driver.find_element(By.XPATH,
                                     f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[9]').text
    low_price = driver.find_element(By.XPATH,
                                    f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[10]').text
    trade_volume = driver.find_element(By.XPATH,
                                       f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[11]').text
    driver.execute_script("arguments[0].scrollBy(500, 0)", scroll)
    trade_amount = driver.find_element(By.XPATH,
                                       f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[12]').text
    market_cap = driver.find_element(By.XPATH,
                                     f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[13]').text
    listed_shares = driver.find_element(By.XPATH,
                                        f'/html/body/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{tr}]/td[14]').text

    if price_diff_img.get_attribute('src') == 'https://data.krx.co.kr/templets/mdc/img/ico_updown1.png':
        plus_or_minus = '+'
    else:
        plus_or_minus = '-'

    stock_list.append([stock_code, stock_name, market_type, belonging_department, closing_price,
                       plus_or_minus + price_diff, percent_change, opening_price, high_price, low_price, trade_volume,
                       trade_amount, market_cap, listed_shares])

    if tr % 52 == 0:
        tr -= 26
    tr += 1

    driver.execute_script("arguments[0].scrollBy(-500, 28)", scroll)

print(stock_list)
driver.quit()
