from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from .models import Stock, Price

import pandas as pd
import csv

from .utils import get_chart

# Create your views here.
# def index(request):
#     context = {"stock_name": "삼성전자", "listed_date": "1975/06/11", "dividend_date": "2023/04/14", "dividend_amount": "362원"}

#     return render(request, "stock_analyze/index.html", context)

def index(request):

    # CSV 데이터 모델에 저장
    with open('stocks.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # 첫번째 행은 헤더이므로 건너뜁니다.

        for row in reader:
            # 각 행의 데이터를 읽어옵니다.

            # stock_name = row[0]
            # standard_code = row[1]
            # listing_date = datetime.strptime(row[2], '%Y-%m-%d')
            # dividend_date = datetime.strptime(row[3], '%Y-%m-%d') if row[3] else None
            # dividend_amount = int(row[4]) if row[4] else None
            # face_value = int(row[5])
            # num_of_stocks = int(row[6])
            # open_price = int(row[7])
            # close_price = int(row[8])
            # high_price = int(row[9])
            # low_price = int(row[10])

            stock_name = "삼성전자"
            standard_code = "005930"
            listing_date = "2018-01-01"
            dividend_date = "2018-01-02"
            dividend_amount = 599
            face_value = 50
            num_of_stocks = 1000

            date = datetime.strptime(row[0], "%Y.%m.%d").date()

            # open_price = int(row[3])
            # close_price = int(row[1])
            # high_price = int(row[4])
            # low_price = int(row[5])

            open_price = int(row[3][0:2] + row[3][3:])
            close_price = int(row[1][0:2] + row[1][3:])
            high_price = int(row[4][0:2] + row[4][3:])
            low_price = int(row[5][0:2] + row[5][3:])
            
            # Stock 객체를 생성합니다.
            stock, created = Stock.objects.get_or_create(
                stock_name=stock_name,
                standard_code=standard_code,
                listing_date=listing_date,
                face_value=face_value,
                num_of_stocks=num_of_stocks,
            )

            # Price 객체를 생성합니다.
            price = Price(
                stock=stock,
                date=date,
                open_price=open_price,
                close_price=close_price,
                high_price=high_price,
                low_price=low_price,
            )

            if dividend_date and dividend_amount:
                price.dividend_date = dividend_date
                price.dividend_amount = dividend_amount

            price.save()

    # 모델 데이터 가져오기
    stock_data = Stock.objects.all()
    price_data = Price.objects.all()

    print()
    print()
    print()
    print(price_data.values()[0])
    print()
    print()

    price_data_df = pd.DataFrame(price_data.values())[["date", "close_price"]]
    price_data_df["date"] = price_data_df["date"].apply(lambda x : pd.to_datetime(str(x).split()[0]))
    print(price_data_df.head())
    chart = get_chart(price_data_df)


    return render(request, "stock_analyze/index.html", {"stock_data": stock_data, "price_data": price_data, "chart":chart})    


# 검색 기능
# def search(request):
#     if 'company_name' in request.GET:
#         company_name = request.GET['company_name']
#         data = Stock.objects.filter(company_name__icontains=company_name).order_by('date')
#         if data:
#             prices = list(data)
#             market_cap = data.aggregate(Sum('market_cap'))['market_cap__sum']
#             return render(request, 'search.html', {'company_name': company_name, 'prices': prices, 'market_cap': market_cap})
#     return render(request, 'search.html')




# 차트 만드는 코드