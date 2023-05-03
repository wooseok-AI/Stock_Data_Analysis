import csv
import matplotlib.pyplot as plt

start = input()
end = input()

# csv 파일에서 데이터 읽어오기
with open('samsung_3y.csv', 'r', encoding='cp949') as f:
    reader = csv.reader(f)
    header = next(reader)  # 첫 줄은 header로 읽어옴
    data = [row for row in reader]

# 데이터를 x, y 축으로 나누기
dates = [row[0] for row in data]
prices = [int(row[4]) for row in data]

start_idx = dates.index(start)
end_idx = dates.index(end)

x_data = dates[start_idx:end_idx:-1]
y_data = prices[start_idx:end_idx:-1]

# 그래프 그리기
plt.plot(x_data, y_data)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Samsung Electronics Stock Prices')
plt.xticks(x_data[::21], rotation=45) # x축 눈금을 한달 간격으로 하기 위해 21일 간격으로 눈금을 표시했습니다.

plt.show()
