from django.core.management.base import BaseCommand

from datetime import datetime
from ...models import Stock, Price

import csv

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open('all_info.csv', 'r', encoding='euc-kr') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    stock_name = row[2]
                    standard_code = row[0]
                    listing_date = datetime.strptime(row[5], '%Y/%m/%d')

                    try:
                        face_value = int(row[10])

                    except:
                         face_value = 0

                    num_of_stocks = row[11]

                    stock, created = Stock.objects.get_or_create(
                        stock_name=stock_name,
                        standard_code=standard_code,
                        listing_date=listing_date,
                        face_value=face_value,
                        num_of_stocks=num_of_stocks,
                    )

                    stock.save()

        # CSV 데이터 모델에 저장
        with open('stocks.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # 첫번째 행은 헤더이므로 건너뜁니다.

            for row in reader:
                date = datetime.strptime(row[0], "%Y.%m.%d").date()

                open_price = int(row[3][0:2] + row[3][3:])
                close_price = int(row[1][0:2] + row[1][3:])
                high_price = int(row[4][0:2] + row[4][3:])
                low_price = int(row[5][0:2] + row[5][3:])
            

                # Price 객체를 생성합니다.
                price = Price(
                    date=date,
                    open_price=open_price,
                    close_price=close_price,
                    high_price=high_price,
                    low_price=low_price,
                )

                price.save()
