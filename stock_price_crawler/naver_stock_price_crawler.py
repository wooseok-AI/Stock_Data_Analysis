import requests
from bs4 import BeautifulSoup
import csv


def add_stocks(tds):
    count = 0
    stocks = []
    for i,x in enumerate(tds):
        data = x.text.strip()
        if len(stocks) == 10:
            break
        elif data:
            count += 1
            if count % 7 == 1:
                date = data
            if count % 7 == 2:
                closing_price = data
            if count % 7 == 3:
                prev_price_diff = data
            if count % 7 == 4:
                opening_price = data
            if count % 7 == 5:
                high_price = data
            if count % 7 == 6:
                low_price = data
            if count % 7 == 0:
                volume = data
                #print([date, closing_price, prev_price_diff, opening_price, high_price, low_price, volume])
                stocks.append([str(date), closing_price, prev_price_diff, opening_price, high_price, low_price, volume])
        else:
            continue
    return stocks


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

full_stocks = []
for page in range(1, 11):
    url = "https://finance.naver.com/item/sise_day.naver?code=005930&page={}".format(page)

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    tds = soup.find_all("td")
    full_stocks += add_stocks(tds)


#print(full_stocks)
with open("stocks.csv", "w", encoding="utf-8") as f:
    fields = ['date', 'closing_price', 'prev_price_diff', 'opening_price', 'high_price', 'low_price', 'volume']

    writer = csv.writer(f)

    writer.writerow(fields)
    writer.writerows(full_stocks)
