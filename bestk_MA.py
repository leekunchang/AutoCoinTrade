import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-ETH", count=90)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)
    # 이동평균선 3일기준 추가(window=고려일수)
    df['ma5'] = df['close'].rolling(window=3).mean().shift(1)
    # bull = 전일종가 > 이평선보다 높을경우 TRUE
    df['bull'] = df['open'] > df['ma5']

    fee = 0.0005
    df['ror'] = np.where((df['high'] > df['target']) & df['bull'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close'] / df['target'] - fee,
                      1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))