import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from core.user_agent import get_random_user_agent


def get_histogram(item_nameid):
    url = f"https://steamcommunity.com/market/itemordershistogram?country=TR&language=english&currency=1&item_nameid={item_nameid}"
    headers = {
        "User-Agent": get_random_user_agent()
    }
    response = requests.get(url,headers=headers,timeout=10)
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return {
                "success":True,
                "lowest_sell_order": float(data["lowest_sell_order"]),
                "highest_buy_order": float(data["highest_buy_order"])
            }
    return {"success":False}
def get_listing_price(item_nameid):
    return get_histogram(item_nameid)