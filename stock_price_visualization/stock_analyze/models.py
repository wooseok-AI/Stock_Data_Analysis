from django.db import models

class Stock(models.Model):
    stock_name = models.CharField(max_length = 50)

    # 표준코드
    standard_code = models.CharField(max_length = 20, default = "000000") 

    # 상장일
    listing_date = models.DateField(null = True)

    # 배당일, 배당금
    dividend_date = models.DateField(null = True)
    dividend_amount = models.IntegerField(null = True)

    # 액면가
    face_value = models.IntegerField(default = 0)

    # 상장주식수
    num_of_stocks = models.IntegerField(default = 0)

class Price(models.Model):
    # stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    date = models.DateTimeField()

    # 시가, 종가, 최고가, 최저가
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    company_name = models.CharField(max_length = 20, default = "")