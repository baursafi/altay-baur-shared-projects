NVDA_price_20250925 = 177.69
NVDA_price_20250101 = 138.31
NVDA_price_20240101 = 49.10
relative_delta = round(((NVDA_price_20250925 / NVDA_price_20250101) - 1) * 100, 2)
print(f"relative change from initial price is {relative_delta}%")
yearly_revenue_2024 = 60920000000
yearly_revenue_2023 = 26970000000

revenue_growth = round((yearly_revenue_2024/yearly_revenue_2023), 2)
price_growth = round((NVDA_price_20250101/NVDA_price_20240101), 2)
print(revenue_growth, price_growth)
#To-Do List:
#Explain why share price growth is faster than revenue growth
#Calculate what will be the expected price for NVDA shares on 01/01/26