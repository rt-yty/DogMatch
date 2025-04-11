from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, UserAnswers
from flask_migrate import Migrate
import uuid

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-answer', methods=['POST'])
def save_answer():
    data = request.get_json()

    if not data or 'question' not in data or 'answer' not in data:
        return jsonify({"error": "Некорректные данные"}), 400

    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())

    user_answers = UserAnswers.query.get(user_id)

    if not user_answers:
        user_answers = UserAnswers(id=user_id)
        db.session.add(user_answers)

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
        "Насколько вы стрессоуствоичивый человек?": "ans11",
        "Хотели бы заняться охотой?": "ans12",
        "Насколько важна для вас тишина?": "ans13",
        "Вы любите путешествовать?": "ans14",
    }

    field_name = question_map.get(data['question'])
    if field_name:
        setattr(user_answers, field_name, data['answer'])
    
    db.session.commit()

    response = jsonify({"message": "Ответ сохранён", "user_id": user_id})
    response.set_cookie('user_id', user_id, max_age=60*60*24*30)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
