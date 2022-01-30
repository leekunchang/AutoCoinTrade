import time
import pyupbit
import datetime

access = "K1izlIYmgptIBMaMhfaZlWh8KlFnUXOxIXmS91pA"
secret = "x4vnFWp8mViKuunhEZwkAaojIomtTNnzVx6xMIDi"

K_code = 0.3 # K 상수값
# coin_code = "KRW-SAND"



def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker): # MA버전 추가분
    """3일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=3)
    ma15 = df['close'].rolling(3).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작s
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-SNAD")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", K_code) # K상수값 K_code
            ma15 = get_ma15("KRW-SAND") # MA버전 삽입분
            current_price = get_current_price("KRW-SAND")
            benefit_price = target_price * 1.15 # 익절조건은 매수 후 15%상승시
            if target_price < current_price and ma15 < current_price and current_price < benefit_price: # MA버전 삽입분
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.9995)
            elif target_price < current_price and benefit_price < current_price: # 익절코드
                sand = get_balance("SAND")
                if sand > 0.00008:
                    upbit.sell_market_order("KRW-SAND", sand*0.9995)
                    break
        else:
            sand = get_balance("SAND")
            if sand > 0.00008:
                upbit.sell_market_order("KRW-SAND", sand*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
