from core.scraper import get_listing_price
import json
name_input = input("Please enter the item name:")
with open("cs2.json","r",encoding="utf-8") as file:
    item_map = json.load(file)
item_nameid = item_map.get(name_input)
result = get_listing_price(item_nameid)
if result["success"]:
    raw_lowest_sell = (result["lowest_sell_order"])/100
    raw_highest_buy = (result["highest_buy_order"])/100
    formatted_lowest_sell = f"{raw_lowest_sell:,.2f}"
    formatted_highest_buy = f"{raw_highest_buy:,.2f}"
    print("🔻 Lowest Sell:", formatted_lowest_sell)
    print("🔺 Highest Buy:", formatted_highest_buy)
    
    
