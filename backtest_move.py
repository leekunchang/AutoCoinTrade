import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터 - 1분봉 200분치
df = pyupbit.get_ohlcv("KRW-SOL","minute1",3600)

# 60분 뒤 종가
df['close60'] = df['close'].shift(-10)

# 이동평균선 5분기준 추가(window=고려일수)
df['ma5'] = df['close'].rolling(window=5).mean().shift(0)

# 이동평균선 10분기준 추가(window=고려일수)
df['ma10'] = df['close'].rolling(window=10).mean().shift(0)

# 이동평균선 20분기준 추가(window=고려일수)
df['ma20'] = df['close'].rolling(window=20).mean().shift(0)

# 이동평균선 60분기준 추가(window=고려일수)
df['ma60'] = df['close'].rolling(window=60).mean().shift(0)

# 이동평균선 120분기준 추가(window=고려일수)
df['ma120'] = df['close'].rolling(window=120).mean().shift(0)

# 변동폭 * k 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

df['sellingprice'] = df['target'] * 1.0105

# bull = 전일종가 > 이평선보다 높을경우 TRUE -> ##내용변경 이평 5분이 이평 10분보다 클경우로 변경
df['bull10'] = df['ma5'] > df['ma10']

df['bull20'] = df['ma5'] > df['ma20']

df['bull60'] = df['ma5'] > df['ma60']

df['bull120'] = df['ma5'] > df['ma120']


# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
fee = 0.0005
df['ror10'] = np.where((df['high'] > df['target']) & df['bull10'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close60'] / df['target'] - fee,
                      1)

df['ror20'] = np.where((df['high'] > df['target']) & df['bull20'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close60'] / df['target'] - fee,
                      1)                      

df['ror60'] = np.where((df['high'] > df['target']) & df['bull60'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close60'] / df['target'] - fee,
                      1)                      

df['ror120'] = np.where((df['high'] > df['target']) & df['bull120'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close60'] / df['target'] - fee,
                      1)                      

df['benefit'] = np.where((df['high'] > df['target']) & df['bull10'], # 이평선 이상일 경우 값 추출 추가 MA버전 삽입분
                      df['close60'] > df['target'] - fee,
                      1)

# 누적 곱 계산(cumprod) => 누적 수익률
# df['hpr'] = df['ror'].cumprod()

# # Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# #MDD 계산
# print("MDD: ", df['dd'].max())

# #HPR 계산 (기간수익율)
# print("HPR: ", df['hpr'][-2])

#엑셀로 출력
df.to_excel("BTC_200_5.xlsx")
print("ok")