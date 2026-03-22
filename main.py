from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Intentional Feed is alive!"}

@app.get("/feed")
def get_feed():
    return {
        "articles": [
            {
                "title": "How Google hires engineers",
                "source": "HackerNews",
                "url": "https://news.ycombinator.com"
            },
            {
                "title": "Best system design resources",
                "source": "Reddit",
                "url": "https://reddit.com/r/cscareerquestions"
            },
            {
                "title": "10 things I wish I knew before my Google interview",
                "source": "Medium",
                "url": "https://medium.com"
            }
        ]
    }