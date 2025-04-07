# config.py

BASE_URL = "https://play.google.com/store/search?q=health{&c=apps"
CSS_SELECTOR = "[class^='info-container']"
REQUIRED_KEYS = [
    "product_name",
    "company_name",
    "average_scores",
    "total_reviews",
    "customer_name",
    "review_score",
    "review_date",
    "review_text",
]