from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class UserAnswers(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    ans1 = db.Column(db.String(255), nullable=True)
    ans2 = db.Column(db.String(255), nullable=True)
    ans3 = db.Column(db.String(255), nullable=True)
    ans4 = db.Column(db.String(255), nullable=True)
    ans5 = db.Column(db.String(255), nullable=True)
    ans6 = db.Column(db.String(255), nullable=True)
    ans7 = db.Column(db.String(255), nullable=True)
    ans8 = db.Column(db.String(255), nullable=True)
    ans9 = db.Column(db.String(255), nullable=True)
    ans10 = db.Column(db.String(255), nullable=True)
    ans11 = db.Column(db.String(255), nullable=True)
    ans12 = db.Column(db.String(255), nullable=True)
    ans13 = db.Column(db.String(255), nullable=True)
    ans14 = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<UserAnswers {self.id}>"
