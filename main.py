from core.scraper import get_listing_price
from alerts.telegram_alert import send_telegram_alert
from dotenv import load_dotenv
from urllib.parse import quote 
from concurrent.futures import ThreadPoolExecutor
import os
import json
import time
item_list = []
commission_rate = 0.13
min_profit = 0.05
with open("item_list.txt","r",encoding="utf-8") as f:
    item_list = [line.strip() for line in f]

with open("cs2.json","r",encoding="utf-8") as file:
        item_map = json.load(file)
def process_item(item):
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
            net_buy_price = raw_highest_buy * (1 - commission_rate)
            profit = net_buy_price - raw_lowest_sell
            if profit > min_profit:
                print("✅ Real Arbitrage Opportunity")
                item_encoded = quote(item)
                url = f"https://steamcommunity.com/market/listings/730/{item_encoded}"

                alert_msg = (
                    f"🟢 BUY ALERT!\n"
                    f"{item}\n"
                    f"🔻 Lowest Sell: {formatted_lowest_sell} USD\n"
                    f"🔺 Highest Buy: {formatted_highest_buy} USD\n"
                    f"{url}"
                )
                send_telegram_alert(alert_msg,TELEGRAM_BOT_TOKEN,CHAT_ID)

        else:
            print(f"{item} couldn't be found.")
        
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
if __name__ == "__main__":
    while True:
       with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(process_item, item_list)

        time.sleep(300)  