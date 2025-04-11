# DogMatch — Рекомендательный сервис для подбора породы собаки

DogMatch — это веб-сервис, который помогает подобрать идеальную породу собаки на основе анкеты пользователя. Система анализирует ответы пользователя и сравнивает их с характеристиками пород, чтобы рекомендовать 10 наиболее подходящих вариантов с процентным рейтингом.

---

## Как это работает?

1. **Анкета пользователя:**
   - Пользователь отвечает на 14 вопросов (например, где живете, насколько вы активны, какой климат предпочитаете и т.д.).
   - Ответы преобразуются в числовые значения от 0 до 1 (например, "прохладный климат" → 0.5).

2. **Параметры пород:**
   - Каждая порода описана набором числовых характеристик, соответствующих каждому из 14 вопросов.
   - Параметры нормализуются в диапазоне от 0 до 1.

3. **Нейросетевая оценка совместимости:**
   - Вектор ответов пользователя (14 чисел) и вектор параметров породы (14 чисел) объединяются в один вектор (28 чисел).
   - Объединённый вектор передаётся через полносвязную (MLP) сеть, которая предсказывает одно число — оценку совместимости (от 0 до 1).
   - В качестве цели (псевдо-лейблы) используется эвристика:
     
     ```
     ideal_score = (1/14) * Σ (1 - |user_i - breed_i|)
     ```
     
   - Модель обучается минимизировать разницу между предсказанной оценкой и этой идеальной оценкой.

4. **Рекомендация:**
   - При использовании модели, вектор ответов пользователя сравнивается с параметрами каждой из 350 пород.
   - Вычисляются оценки совместимости, породы сортируются, и отображаются топ-10 вариантов с процентными значениями (после нормализации через softmax).

---

## Технологии

- **Backend:** Flask, SQLAlchemy, PostgreSQL  
- **Frontend:** HTML, CSS, JavaScript  
- **Нейронная сеть:** PyTorch (MLP для оценки совместимости)  
- **Идентификация пользователя:** UUID, cookies