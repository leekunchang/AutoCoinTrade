# k = 300
# x = 150


# if k > 100:
#     if x > 200:
#         print("1단계 조건충족")
# if k * 2 > 100:
#     if x > 50:
#         print("2단계 조건충족")

#     if target_price < current_price and target_price * 1.2 < current_price:
#         krw = get_balance("KRW")
#         if krw > 5000:
#             upbit.buy_market_order("KRW-BTC", krw * 0.9995)
#     elif target_price < current_price and target_price * 1.2 > current_price: 
#         btc = get_balance("BTC")
#         if btc > 0.00008: 
#             upbit.sell_market_order("KRW-BTC", btc * 0.9995)
#     else:
#         print("Do nothing")
# else:
#     btc = get_balance("BTC")
#     if btc > 0.0008:
#         upbit.sell_market_order("KRW-BTC", btc * 0.9995)
        
# time.sleep(1);


# 1번 현재가 100 = 거래 안되어야함
# 2번 현재가 201 = 매수 되어야함
# 3번 현재가 250 = 익절 되어야함

# current1 = 250
# target1 = 200
# if target1 < current1 and target1 * 1.2 > current1:
#     print("매수")
# elif target1 < current1 and target1 * 1.2 < current1:
#     print("익절")
# else:
#     print("안사")
    
# 변수 깔끔하게 버전
previusPrice = 200 # 1차 매수 희망값
currentPrice = 250 # 현재가
targetPrice = previusPrice * 1.2 # 익절 희망가, 상수부분 희망 익절배율로
# 현재가격이 100이면 안사
# 현재가격이 201이면 매수
# 현재가격이 250이면 익절


if previusPrice < currentPrice and currentPrice < targetPrice:
    print("매수")
elif previusPrice < currentPrice and targetPrice < currentPrice:
    print("익절")
else:
    print("안사")