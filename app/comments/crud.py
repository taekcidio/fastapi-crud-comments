from sqlalchemy.orm import Session
from . import models, schemas

OFFENSIVE_WORDS = {"idiota", "tonto", "estúpido", "feo", "lento"}
POSITIVE_WORDS = {"excelente", "me encanta", "felicidades", "bueno", "gracias"}
NEGATIVE_WORDS = {"horrible", "odio", "asco", "terrible", "pésimo"}

def classify_comment(content: str) -> str:
    if any(word in content.lower() for word in OFFENSIVE_WORDS):
        return "rejected"
    return "approved"

def analyze_sentiment(content: str) -> str:
    content = content.lower()
    if any(word in content for word in POSITIVE_WORDS):
        return "positive"
    if any(word in content for word in NEGATIVE_WORDS):
        return "negative"
    return "neutral"

def create_comment(db: Session, comment: schemas.CommentCreate):
    status = classify_comment(comment.content)
    sentiment = analyze_sentiment(comment.content)
    db_comment = models.Comment(content=comment.content, status=status, sentiment=sentiment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_all_comments(db: Session):
    return db.query(models.Comment).all()

def get_stats(db: Session):
    from sqlalchemy import func
    total = db.query(func.count(models.Comment.id)).scalar()
    approved = db.query(func.count()).filter(models.Comment.status == "approved").scalar()
    rejected = db.query(func.count()).filter(models.Comment.status == "rejected").scalar()
    positives = db.query(func.count()).filter(models.Comment.sentiment == "positive").scalar()
    negatives = db.query(func.count()).filter(models.Comment.sentiment == "negative").scalar()
    neutrals = db.query(func.count()).filter(models.Comment.sentiment == "neutral").scalar()
    return {
        "total_comments": total,
        "approved": approved,
        "rejected": rejected,
        "positives": positives,
        "negatives": negatives,
        "neutrals": neutrals
    }
