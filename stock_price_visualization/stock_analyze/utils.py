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

def get_png():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(chart_type = "line_plot", data, **kwargs):
    
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10,4))

    if chart_type == "line_plot":
        plt.plot(data["date"], data["closing_price"], color="navy", linewidth=3)
    elif chart_type == "box_plot":
        pass
    
    plt.tight_layout()
    chart = get_png()

    return chart

    
# def generate_code():
#     return str(uuid.uuid4()).replace('-', '').upper()[:12]


# def get_key(res_by):
#     if res_by == '#1':
#         key = 'transaction_id'
#     elif res_by == '#2':
#         key = 'created'
#     elif res_by == '#3':
#         key = 'customer'
#     elif res_by == '#4':
#         key = 'total_price'

#     return key


# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph


# def get_chart(chart_type, data, results_by, **kwargs):
#     plt.switch_backend('AGG')
#     fig = plt.figure(figsize=(10, 4))
#     key = get_key(results_by)
#     d = data.groupby(key, as_index=False)['total_price'].agg('sum')

#     if chart_type == '#1':
#         print("Bar Graph")
#         plt.bar(d[key], d['total_price'])
#     elif chart_type == '#2':
#         print("Pie chart")
#         plt.pie(data=d, x='total_price', labels=d[key])
#     elif chart_type == '#3':
#         print("Line graph")
#         plt.plot(d[key], d['total_price'], color='gray', marker='o', linestyle='dashed')
#     else:
#         print("차트 타입이 선택되지 않았습니다")


#     plt.tight_layout()
#     chart = get_graph()

#     return chart