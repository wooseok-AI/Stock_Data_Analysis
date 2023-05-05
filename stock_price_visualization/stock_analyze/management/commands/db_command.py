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

        # CSV ������ �𵨿� ����
        with open('stocks.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # ù��° ���� ����̹Ƿ� �ǳʶݴϴ�.

            for row in reader:
                date = datetime.strptime(row[0], "%Y.%m.%d").date()


                open_price = int("".join(row[3].split(",")))
                close_price = int("".join(row[1].split(",")))
                high_price = int("".join(row[4].split(",")))
                low_price = int("".join(row[5].split(",")))
                # open_price = int(row[3][0:2] + row[3][3:])
                # close_price = int(row[1][0:2] + row[1][3:])
                # high_price = int(row[4][0:2] + row[4][3:])
                # low_price = int(row[5][0:2] + row[5][3:])
            

                # Price ��ü�� �����մϴ�.
                price = Price(
                    date=date,
                    open_price=open_price,
                    close_price=close_price,
                    high_price=high_price,
                    low_price=low_price,
                )

                price.save()
