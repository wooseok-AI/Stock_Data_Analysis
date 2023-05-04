# Stock_Price_Visualization

해당 프로젝트는 주식 가격에 대한 기간 별 검색 및 다양한 차트의 반환을 목표로 [Django](https://www.djangoproject.com/)를 이용한 서비스의 형태로 개발하였으며, [Grepp] KDT 데이터 엔지니어링 데브코스에서 진행하는 1차 프로젝트 결과물의 일환이다. <br>


![Default Home View](__screenshots/home.png?raw=true "Title")

| Features

-


## Requirements
---
```bash
asgiref==3.6.0
coverage==7.2.5
Django==4.2
djangorestframework==3.14.0
pytz==2023.3
sqlparse==0.4.4
pandas==1.5.2
matplotlib==3.6.2
selenium~=4.8.3
requests~=2.28.2
beautifulsoup4~=4.12.2
mplfinance~=0.12.9b7
```

## How to use it
---
<p><strong> 1. Basic Setting</strong></p>

```bash
# Get the Code
$ git clone https://github.com/wooseok-AI/Stock_Data_Analysis
$ cd Stock_Data_Analysis

# Virtualenv module Installation (Unix Based systems)
$ virtualenv env
$ source env/bin/activate

# Virtualenv modules installation (Windows based systems)
# virtualenv env
# .\env\Scripts\activate

# Install modules
$ pip3 install -r requirements.txt
```
<br>
<p><strong> 2. How to Use Crawler </strong><p>

```bash
$ cd stock_price_crawler

# KRX 기반 주식 데이터 크롤
$ python krx_stock_price_crawler.py

# Naver 주식 기반 데이터 크롤
$ python naver_stock_price_crawler.py
```

<p><strong> 3. How to Run Django Service</strong></p>

```bash
# Create Tables from stocks.csv
$ python manage.py db_command
$ python manage.py makemigrations
$ python manage.py migrate
 
# Start the application (development mode)
$ python manage.py runserver # default port 8000

# Start the app - custom port
$ python manage.py runserver 0.0.0.0:<your_port>
$
# Access the web app in browser: http://127.0.0.1:8000/
```

<br>

# Codebase Structure

```bash
<PROJECT ROOT>

 README.md
├── matplotlib
│   ├── samsung_3y.csv
│   └── visual.py
├── requirements.txt
├── stock_price_crawler
│   ├── krx_stock_price_crawler.py
│   ├── naver_stock_price_crawler.py
│   ├── stocks.csv
│   └── visualization.ipynb
└── stock_price_visualization
    ├── all_info.csv
    ├── db.sqlite3
    ├── manage.py
    ├── stock_analyze
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── management
    │   │   └── commands
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   ├── __init__.cpython-39.pyc
    │   │       │   └── db_command.cpython-39.pyc
    │   │       └── db_command.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templates
    │   │   └── stock_analyze
    │   │       ├── index.html
    │   │       └── stock.html
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    ├── stock_price_visualization
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── settings.cpython-39.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   └── wsgi.cpython-39.pyc
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── stocks.csv
```
