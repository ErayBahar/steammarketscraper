from core.scraper import get_listing_price
import json
item_list = []
with open("item_list.txt","r",encoding="utf-8") as f:
    data = f.readlines()
for line in data:
    item_list.append(line.strip())
with open("cs2.json","r",encoding="utf-8") as file:
    item_map = json.load(file)
for item in item_list:

    item_nameid = item_map.get(item)
    result = get_listing_price(item_nameid)
    if result["success"]:
        raw_lowest_sell = (result["lowest_sell_order"])/100
        raw_highest_buy = (result["highest_buy_order"])/100
        formatted_lowest_sell = f"{raw_lowest_sell:,.2f}"
        formatted_highest_buy = f"{raw_highest_buy:,.2f}"
        print(f"{item}: ")
        print("🔻 Lowest Sell:", formatted_lowest_sell)
        print("🔺 Highest Buy:", formatted_highest_buy)
    else:
        print(f"{item} couldn't be found.")
    
    
