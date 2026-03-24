from fastapi import FastAPI
import requests

app = FastAPI()

MY_INTERESTS = ["AI", "startup", "coding", "python", "machine learning", 
                "software", "developer", "programming", "tech", "google"]

def fetch_hackernews():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_ids = requests.get(top_stories_url, timeout=10).json()
    
    articles = []
    for story_id in top_ids[:30]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url, timeout=10).json()
        
        if story and "title" in story:
            articles.append({
                "title": story.get("title", "No title"),
                "source": "HackerNews",
                "url": story.get("url", "https://news.ycombinator.com"),
                "score": story.get("score", 0)
            })
    
    return articles

def filter_by_interests(articles, interests):
    filtered = []
    for article in articles:
        title = article["title"].lower()
        for interest in interests:
            if interest.lower() in title:
                filtered.append(article)
                break
    return filtered

@app.get("/")
def home():
    return {"message": "Intentional Feed is alive!"}

@app.get("/feed")
def get_feed():
    articles = fetch_hackernews()
    filtered_articles = filter_by_interests(articles, MY_INTERESTS)
    return {
        "interests": MY_INTERESTS,
        "total_found": len(filtered_articles),
        "articles": filtered_articles
    }

@app.get("/feed/{topic}")
def get_feed_by_topic(topic: str):
    articles = fetch_hackernews()
    filtered_articles = filter_by_interests(articles, [topic])
    return {
        "topic": topic,
        "total_found": len(filtered_articles),
        "articles": filtered_articles
    }