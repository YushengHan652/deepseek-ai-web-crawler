from pydantic import BaseModel


class HealthProductReview(BaseModel):
    """
    Represents the data structure of a health product review.
    """

    product_name: str
    company_name: str
    average_scores: float
    total_reviews: int
    customer_name: str
    review_score: int
    review_date: str
    review_text: str
