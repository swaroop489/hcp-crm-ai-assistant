from datetime import datetime
from app.core.constants import SentimentEnum

def parse_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else datetime.now().date()
    except:
        return datetime.now().date()

def parse_time(time_str: str):
    try:
        return datetime.strptime(time_str, "%H:%M").time() if time_str else datetime.now().time()
    except:
        return datetime.now().time()

def parse_sentiment(sentiment_str: str) -> SentimentEnum:
    s = sentiment_str.lower()
    if s == "positive":
        return SentimentEnum.POSITIVE
    elif s == "negative":
        return SentimentEnum.NEGATIVE
    return SentimentEnum.NEUTRAL
