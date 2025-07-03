# 🎯 Steam Sniper Bot (CS2 Edition)

A Python bot that tracks real-time Steam Marketplace prices for CS2 skins using Steam’s hidden `itemordershistogram` endpoint.

It lets you:
- Monitor **lowest sell** and **highest buy** prices
- Track **any skin, agent, or item** using `item_nameid`
- Get Telegram alerts when a sell order is below a buy order (sniping opportunity)

---

## ⚙️ Features

✅ Fast price tracking via Steam's histogram API  
✅ Supports all CS2 items using a local `cs2.json` index  
✅ Item list loaded from `item_list.txt`  
✅ Sends real-time **Telegram alerts**  
✅ Fully local — no browser required  
✅ Easily expandable with SQLite logging or dashboards

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/steammarketscraper.git
cd steammarketscraper
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
venv\\Scripts\\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your `.env` file:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

5. Add item names to `item_list.txt` (each line = 1 item name from cs2.json)

6. Run the bot:

```bash
python main.py
```

If a sell order is **lower** than the highest buy, you’ll get:

```
🟢 BUY OPPORTUNITY!
🔻 Lowest Sell: 3.20 USD
🔺 Highest Buy: 3.45 USD
```

And an alert is sent to Telegram.

---

## 📁 Project Structure

```
steammarketscraper/
├── main.py
├── item_list.txt
├── cs2.json
├── .env
├── requirements.txt
├── core/
│   ├── scraper.py
│   └── user_agent.py
└── alerts/
    └── telegram_alert.py
```

---

## 📦 Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`
- `python-dotenv`

---

## 📜 License

MIT License. Educational and unofficial. Not affiliated with Valve.
