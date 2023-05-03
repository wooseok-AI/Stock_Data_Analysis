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