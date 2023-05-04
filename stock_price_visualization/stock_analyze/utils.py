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
        plt.plot(data["date"], data["close_price"], color="navy", linewidth=3)
    elif chart_type == "bar_plot":
        plt.bar(data["date"], data["close_price"], color="navy", linewidth=3)
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
    if chart_type in ('line_plot', 'bar_plot'):
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
