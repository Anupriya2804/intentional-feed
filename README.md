# Intentional Feed

I was tired of scrolling useless things all day — nothing meaningful, 
nothing related to my goals, no real insights about what's actually 
happening in the world. Just living in a delusional bubble.

So I built my own feed.

**Live → [intentional-feed.vercel.app](https://intentional-feed.vercel.app)**

---

## What it does

Pulls real articles from HackerNews, filters them by topics you 
actually care about, and gives you 20 minutes. When the timer hits 
zero — it locks. No endless scrolling. No algorithm deciding what 
you see. Just content relevant to where you want to go.

---

## How it works

1. You set your interests — AI, coding, startups, anything
2. Backend fetches top stories from HackerNews live
3. Filters out everything that doesn't match your topics
4. Shows clean article cards in the browser
5. 20 minute timer runs — when it hits zero, feed locks

---

## Tech Stack

| | |
|--|--|
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Data | HackerNews API |
| Deployed on | Render + Vercel |

---

## API
GET /feed              → articles filtered by your interests
GET /feed/{topic}      → search any topic live

Try it:
https://intentional-feed.onrender.com/feed/AI
https://intentional-feed.onrender.com/feed/python

---

## Run it locally

```bash
git clone https://github.com/Anupriya2804/intentional-feed.git
cd intentional-feed
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `index.html` in your browser.

---

## Change your interests

In `main.py`:

```python
MY_INTERESTS = ["AI", "startup", "coding", "python", "machine learning"]
```

Add whatever topics matter to you.

---

## What's coming

- YouTube and Instagram integration — one feed across every platform
- User accounts — save your interests
- Mobile layout

---

## Built by

Anupriya — CS undergrad, Ex-intern DRDO

[GitHub](https://github.com/Anupriya2804) · 
[LinkedIn](https://linkedin.com/in/anupriya-sihag)
