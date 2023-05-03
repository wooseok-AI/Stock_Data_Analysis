# from matplotlib import pyplot as plt

# 차트 만드는 코드
# def get_chart():

import pandas
import base64
import uuid
from .models import *
from io import BytesIO
import matplotlib.pyplot as plt


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

    plt.tight_layout()
    chart = get_png(fig)

    return chart


def get_png(fig):
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
