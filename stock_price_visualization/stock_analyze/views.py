from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from .models import Stock, Price

import pandas as pd
import matplotlib.pyplot as plt
import csv

from .utils import get_chart

plt.switch_backend("AGG")

def index(request):
    stock_data = Stock.objects.all()

    return render(request, "stock_analyze/index.html", {"stock_data": stock_data})    

def stock_info(request):
    if request.method == "GET":
        stock_name = request.GET.get("name")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        chart_type = request.GET.get("chart_type")

        print(stock_name, start_date, end_date)
        stock_data = Stock.objects.all()
        print("Request")
        price_data = Price.objects.filter(date__range=[start_date, end_date])
        if price_data.exists():
                price_data_df = pd.DataFrame(price_data.values())

                price_data_df["date"] = price_data_df["date"].apply(lambda x : pd.to_datetime(str(x).split()[0]))
                # price_data_df = price_data_df.groupby("date")["open_price", "close_price", "high_price", "low_price"].last().reset_index()

                fig = plt.figure(figsize=(10, 4))
                chart = get_chart(price_data_df, chart_type=chart_type, fig=fig)

                context = {
                            'stock_data': stock_data,
                            'price_data': price_data_df.to_html(),
                            'chart': chart, 'chart_type': chart_type,
                            'start_date': start_date,
                            'end_date': end_date
                           }
                return render(request, "stock_analyze/stock.html", context)
        else:
            error_message = 'There is no stock data for the specified period.'
            context = {'error_message': error_message}
            return render(request, 'stock_analyze/stock.html', context)
    else:
        error_message = 'Please enter stock name and date range.'
        context = {'error_message': error_message}
        return render(request, 'stock_analyze/stock.html', context)
