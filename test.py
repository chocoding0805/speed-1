import pyupbit

prices = pyupbit.get_current_price(["KRW-ADA", "KRW-LTC"])
print(prices)