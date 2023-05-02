from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"stock_name": "삼성전자", "listed_date": "1975/06/11", "dividend_date": "2023/04/14", "dividend_amount": "362원"}

    return render(request, "stock_analyze/index.html", context)

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