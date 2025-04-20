from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class UserAnswers(db.Model):
    __tablename__ = 'user_answers'

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
    
    question_map = {
        "Вы проживаете в загородном доме или в квартире?": "ans1",
        "Какой у вас образ жизни?": "ans2",
        "У вас были когда-то домашние животные?": "ans3",
        "Сколько в среднем проводите времени вне дома?": "ans4",
        "В каком климате вы проживаете?": "ans5",
        "У вас есть дети?": "ans6",
        "У вас есть на данный момент другая собака?": "ans7",
        "У вас часто бывают дома гости?": "ans8",
        "Насколько сильно вы любите убираться дома?": "ans9",
        "Насколько сильно вы брезгливый человек?": "ans10",
        "Насколько вы стрессоустойчивый человек?": "ans11",
        "Хотели бы заняться охотой?": "ans12",
        "Насколько важна для вас тишина?": "ans13",
        "Вы любите путешествовать?": "ans14",
    }

    def set_answer(self, question_text: str, answer: str) -> None:

        field = self.question_map.get(question_text)
        if not field:
            raise ValueError(f"Неизвестный вопрос: {question_text!r}")
        setattr(self, field, answer)

    def get_answer(self, question_text: str) -> str:

        field = self.question_map.get(question_text)
        if not field:
            return None
        return getattr(self, field)

    def to_dict(self) -> dict:

        return {
            question: getattr(self, field)
            for question, field in self.question_map.items()
        }

    def __repr__(self):
        return f"<UserAnswers {self.id}>"
