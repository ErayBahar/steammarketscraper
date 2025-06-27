# 🎯 Steam Sniper Bot (CS2 Edition)

A Python bot that tracks real-time Steam Marketplace prices for CS2 skins using Steam’s hidden `itemordershistogram` endpoint.

It lets you:
- Monitor **lowest sell** and **highest buy** prices
- Track **any skin, agent, or item** using `item_nameid`
- Build a sniper or alert system for undervalued listings

---

## ⚙️ Features

✅ Fast price tracking via Steam's histogram API  
✅ Supports all CS2 items using a local `cs2.json` index  
✅ Search interface to find item_nameids  
✅ Fully local — no browser required  
✅ Ready to expand with Telegram alerts, SQLite logging, or dashboards

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/steam-sniper-bot.git
cd steam-sniper-bot
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the bot interactively:

```bash
python main.py
```

You’ll be prompted to enter an item name like:

```bash
Please enter the item name: AWP | Asiimov (Field-Tested)
```

If it exists in your `cs2.json`, it will return:

```
🔻 Lowest Sell: 1.321,53 TL
🔺 Highest Buy: 1.210,00 TL
```

---

## 📁 File Structure

```
steam-sniper-bot/
├── main.py
├── cs2.json
├── .env
├── requirements.txt
├── core/
│   ├── scraper.py
│   └── user_agent.py
└── alerts/
    └── telegram.py
```

---

## 🔍 Where to Get `item_nameid`s

You can:
- Extract them via browser DevTools → Network tab → `itemordershistogram?item_nameid=...`
- Use your local `cs2.json` which maps all CS2 item names to their `item_nameid`s

---

## ⚠️ Important Notes

- Steam has rate limits. Avoid hitting endpoints too fast.
- Do not share `cs2.json` or `.env` publicly.

---


## 📦 Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`

---

## 🧠 Future Features

- Telegram / Discord alerts

---

## 📜 License

MIT License. Educational and unofficial. Not affiliated with Valve.
