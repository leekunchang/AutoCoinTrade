import time
import pyupbit
import datetime

access = "K1izlIYmgptIBMaMhfaZlWh8KlFnUXOxIXmS91pA"
secret = "x4vnFWp8mViKuunhEZwkAaojIomtTNnzVx6xMIDi"

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

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-NEAR")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-NEAR", 0.4)
            current_price = get_current_price("KRW-NEAR")
            benefit_price = target_price * 1.2 # 익절조건은 타겟의 1.2배
            if target_price < current_price and current_price < benefit_price: # 타겟금액 이상이되고 익절조건 미만일때 매수만
                krw = get_balance("KRW") # 이하 동일
                if krw > 5000:
                    upbit.buy_market_order("KRW-NEAR", krw*0.9995)
            elif target_price < current_price and benefit_price < current_price: # 타겟금액 이상, 익절조건 이상일때
                near = get_balance("NEAR") # NEAR의 잔고 조회(else: 이하와 동일)
                if near > 0.00008: # near 잔량이 0.00008개 이상 되고
                    upbit.sell_market_order("KRW-NEAR", near*0.9995) # 조건 부합시 매도코드입력. 수수료비용만큼은 제외하고 거래됨)
                    break # 익절 후에는 거래종료 (다시 if조건 안에서 사고 떨어지면 안됨. 추후 9시에 재시작하는 코드 생성예정)
        else:
            near = get_balance("NEAR") # 기존 조건 동일. 9시되면 조건없이 전량매도
            if near > 0.00008:
                upbit.sell_market_order("KRW-NEAR", near*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
