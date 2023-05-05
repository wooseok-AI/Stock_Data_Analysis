import requests
from bs4 import BeautifulSoup
import csv


def add_stocks(tds, end_date):
    count = 0
    stocks = []
    is_end = False

    for i,x in enumerate(tds):
        data = x.text.strip()
        if len(stocks) == 10:
            break
        elif data:
            count += 1
            if count % 7 == 1:
                date = data
                if str(date) < end_date:
                    is_end = True
                    break
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
    return stocks, is_end


stock_id = input('종목코드 : ')
end_date = input('종료일자 ex) 2019.01.01 : ')


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

full_stocks = []
for page in range(1, 109):
    url = "https://finance.naver.com/item/sise_day.naver?code={}&page={}".format(stock_id, page)

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    tds = soup.find_all("td")
    stocks, is_end = add_stocks(tds, end_date)
    full_stocks += stocks

    if is_end:
        break


#print(full_stocks)
with open("{}_stocks.csv".format(stock_id), "w", encoding="utf-8") as f:
    fields = ['date', 'closing_price', 'prev_price_diff', 'opening_price', 'high_price', 'low_price', 'volume']

    writer = csv.writer(f)

    writer.writerow(fields)
    writer.writerows(full_stocks)
