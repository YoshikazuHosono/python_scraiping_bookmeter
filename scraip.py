import time
from selenium import webdriver

# 最大で何ページ取得するか
MAX_PAGE = 5

# Chrome召喚
driver = webdriver.Chrome('C:\\00_BOX\\selenium_driver\\chrome\\win\\83.0.4103.39\\chromedriver.exe')

# 画面遷移
driver.get('https://bookmeter.com/books/580330')
time.sleep(5)

nowPageCount = 0

while nowPageCount < MAX_PAGE:
    # 感想を取得
    for bookImpressionText in driver.find_elements_by_css_selector(".frame__content__text"):
        print('-' * 30)
        print(bookImpressionText.text)

    # 非活性クラスが付与された次へボタンが取得できる場合、最終ページと判定しループを終える
    if len(driver.find_elements_by_css_selector(".pagination-next.disable > a")) != 0:
        break

    # 次へボタン押下
    driver.find_elements_by_css_selector(".pagination-next > a")[0].click()
    time.sleep(5)

    nowPageCount += 1

driver.quit()
