from fastapi import FastAPI
import requests

app = FastAPI()

def fetch_hackernews():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_ids = requests.get(top_stories_url).json()
    articles = []
    for story_id in top_ids[:5]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()
        if story and "title" in story:
            articles.append({
                "title": story.get("title", "No title"),
                "source": "HackerNews",
                "url": story.get("url", "https://news.ycombinator.com"),
                "score": story.get("score", 0)
            })
    return articles

@app.get("/")
def home():
    return {"message": "Intentional Feed is alive!"}

@app.get("/feed")
def get_feed():
    articles = fetch_hackernews()
    return {"articles": articles}