# from matplotlib import pyplot as plt

# 차트 만드는 코드
# def get_chart():

import pandas as pd
import base64
import uuid
from .models import *
from io import BytesIO
import matplotlib.pyplot as plt
import mplfinance as mf


def preprocessing(data):
    """
    Data 가 컬럼별로 리스트 형태로 주어질 경우
    """
    pass


def get_chart(data, chart_type="line_plot", fig=None, **kwargs):
    
    if fig is None:
        fig = plt.figure(figsize=(10, 4))
    if chart_type == "line_plot":
        plt.title("line_plot")
        plt.plot(data["date"], data["close_price"], color="navy", linewidth=3)
    elif chart_type == "bar_plot":
        plt.title("bar_plot")
        plt.bar(data["date"], data["close_price"], color="navy", linewidth=3)
    # 중복 그래프 출력
    elif chart_type == "trend_line":
        # 추세선 그래프
        ma5 = data["close_price"].rolling(window=5).mean()
        ma20 = data["close_price"].rolling(window=20).mean()
        ma60 = data["close_price"].rolling(window=60).mean()
        ma120= data["close_price"].rolling(window=120).mean()

        data.insert(len(data.columns), "MA5", ma5)
        data.insert(len(data.columns), "MA20", ma20)
        data.insert(len(data.columns), "MA60", ma60)
        data.insert(len(data.columns), "MA120", ma120)

        plt.plot(data["date"], data['close_price'], label='Close_price')
        plt.plot(data["date"], data['MA5'], label='5d average')
        plt.plot(data["date"], data['MA20'], label='20d average')
        plt.plot(data["date"], data['MA60'], label='60d average')
        plt.plot(data["date"], data['MA120'], label='120d average')
        plt.legend()

    elif chart_type == "candle_plot":
        data = data.rename(
            columns={'close_price': 'Close', 'open_price': 'Open', 'high_price': 'High', 'low_price': 'Low',
                     'volume': 'Volume'})
        data = data.set_index('date', drop=False)
        data['date'] = data['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
        data.index = pd.DatetimeIndex(data['date'])
        fig = data

    plt.tight_layout()
    chart = get_png(chart_type, fig, data)

    return chart


def get_png(chart_type, fig, data):
    buffer = BytesIO()
    if chart_type in ('line_plot', 'bar_plot', 'trend_line'):
        fig.savefig(buffer, format='png')
    else:
        color_set = mf.make_marketcolors(up='tab:red', down='tab:blue')
        s = mf.make_mpf_style(marketcolors=color_set)
        mf.plot(data, type='candle', style=s, figsize=(10, 4), datetime_format=' %Y-%m-%d', xrotation=0, savefig=dict(fname=buffer, dpi=100, pad_inches=0.25))
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
