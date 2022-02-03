# if target_price < current_price and ma3 < current_price and current_price < benefit_price and current_price < target_price * 1.01:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     upbit.buy_market_order("KRW-"+coin_code, krw*0.9995)
#             elif target_price < current_price and benefit_price < current_price:


# crunt_price_list = [980, 1001, 1009, 1023]
# c1 = [for i in crun
# t_price_list]
# print(c1)

c1 = 1099
t1 = 1000000
ma3 = 980000
b1 = t1 * 1.0205

print("현재가", c1)
print("매수가", t1)
print("재매수가", t1* 1.01)
print("익절값", b1)
print("손절값", t1 * 0.998)

if t1 < c1 and ma3 < c1 and c1 < b1 and c1 < t1 * 1.01:
    print("매수")
elif t1 * 0.998 > c1 or t1 < c1 and b1 < c1:
    print("매도")
else:
    print("안사")
