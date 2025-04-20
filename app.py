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

    user_id = request.cookies.get('user_id') or str(uuid.uuid4())
    
    if not user_id:
        user_id = str(uuid.uuid4())

    user_answers = UserAnswers.query.get(user_id)

    if not user_answers:
        user_answers = UserAnswers(id=user_id)
        db.session.add(user_answers)

    try:
        user_answers.set_answer(data['question'], data['answer'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
        
    db.session.commit()

    response = jsonify({
        "message" : "Ответ сохранен",
        "user_id" : user_id
    })
    response.set_cookie('user_id', user_id, max_age=60*5)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
