from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from datetime import datetime
from .models import Stock, Price

import pandas as pd
import matplotlib.pyplot as plt
import csv

from .utils import get_chart

plt.switch_backend("AGG")

def index(request):
    stock_data = Stock.objects.all()

    paginator = Paginator(stock_data, 30)
    page = request.GET.get("page")

    try:
        stocks = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        stocks = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        stocks = paginator.page(page)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index + 1)

    if int(page) <= 2:
        custom_range = range(1, 6)

    if int(page) >= paginator.num_pages - 2:
        custom_range = range(paginator.num_pages - 4, paginator.num_pages + 1)

    return render(request, "stock_analyze/index.html", {"stocks": stocks, "custom_range": custom_range})    

def stock_info(request):
    if request.method == "GET":
        name_input = request.GET.get("name_input")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        chart_type = request.GET.get("chart_type")

        print(name_input, start_date, end_date)
        stock_data = Stock.objects.all()
        print("Request")
        price_data = Price.objects.filter(date__range=[start_date, end_date]).filter(company_name = name_input)
        if price_data.exists():
                price_data_df = pd.DataFrame(price_data.values())

                price_data_df["date"] = price_data_df["date"].apply(lambda x : pd.to_datetime(str(x).split()[0]))
                print("======REQUEST==========\n\n\n\n", price_data_df.head(), "\n\n\n\n")
                price_data_df = price_data_df.groupby("date")["open_price", "close_price", "high_price", "low_price","company_name"].last().reset_index()
                fig = plt.figure(figsize=(10, 4))
                chart = get_chart(price_data_df, chart_type=chart_type, fig=fig)

                context = {
                            'name_input' : name_input,
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
