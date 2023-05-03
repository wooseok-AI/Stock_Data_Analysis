from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from .models import Stock, Price

import pandas as pd
import csv

from .utils import get_chart


def index(request):

    # 모델 데이터 가져오기
    stock_data = Stock.objects.all()
    price_data = Price.objects.all()

    price_data_df = pd.DataFrame(price_data.values())[["date", "close_price"]]
    price_data_df["date"] = price_data_df["date"].apply(lambda x : pd.to_datetime(str(x).split()[0]))
    
    chart = get_chart(price_data_df)

    return render(request, "stock_analyze/index.html", {"stock_data": stock_data, "price_data": price_data, "chart":chart})    

