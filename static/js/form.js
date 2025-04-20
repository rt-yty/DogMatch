document.addEventListener('DOMContentLoaded', function () {
    const questions = [
      {
        title: "Вы проживаете в загородном доме или в квартире?",
        answers: ["В загородном доме", "В квартире"]
      },
      {
        title: "Какой у вас образ жизни?",
        answers: ["Активный", "Умеренный", "Cпокойный"]
      },
      {
        title: "У вас были когда-то домашние животные?",
        answers: ["Были", "Не были"]
      },
      {
        title: "Сколько в среднем проводите времени вне дома?",
        answers: ["Менее 2 часов", "2-5 часов", "5-8 часов", "8-12 часов", "Более 12 часов"]
      },
      {
        title: "В каком климате вы проживаете?",
        answers: ["Холодный", "Прохладный", "Средний", "Теплый", "Жаркий"]
      },
      {
        title: "У вас есть дети?",
        answers: ["Есть", "Нет"]
      },
      {
        title: "У вас есть на данный момент другая собака?",
        answers: ["Есть", "Нет"]
      },
      {
        title: "У вас часто бывают дома гости?",
        answers: ["Очень часто", "Иногда", "Очень редко"]
      },
      {
        title: "Насколько сильно вы любите убираться дома?",
        answers: ["Очень сильно", "Средне", "Не очень люблю"]
      },
      {
        title: "Насколько сильно вы брезгливый человек?",
        answers: ["Очень сильно", "Не очень", "Вообще нет"]
      },
      {
        title: "Насколько вы стрессоустойчивый человек?",
        answers: ["Мне все ни по чем", "Средне", "Не очень"]
      },
      {
        title: "Хотели бы заняться охотой?",
        answers: ["Определенно да", "Пока не знаю", "Точно нет"]
      },
      {
        title: "Насколько важна для вас тишина?",
        answers: ["Очень важна", "Средне", "Вообще все равно"]
      },
      {
        title: "Вы любите путешествовать?",
        answers: ["Да, очень!", "Иногда куда-то выезжаю", "Почти всегда нахожусь в родном городе"]
      },
    ];
  
    let currentQuestion = 0;
    const tryBtn = document.getElementById('tryBtn');
    const questionForm = document.getElementById('questionForm');
    const questionTitle = document.getElementById('questionTitle');
    const answersContainer = document.getElementById('answersContainer');
    const nextBtn = document.getElementById('nextBtn');
  
    function showQuestion(index) {
      const question = questions[index];
      questionTitle.textContent = question.title;
      answersContainer.innerHTML = '';
      question.answers.forEach(answer => {
        const answerLabel = document.createElement('label');
        const radioInput = document.createElement('input');
        radioInput.type = 'radio';
        radioInput.name = 'answer';
        radioInput.value = answer;
        answerLabel.appendChild(radioInput);
        answerLabel.appendChild(document.createTextNode(" " + answer));
        answersContainer.appendChild(answerLabel);
      });
    }
  
    tryBtn.addEventListener('click', () => {
      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
      });
      setTimeout(() => {
        questionForm.classList.remove('hidden');
        void questionForm.offsetWidth;
        questionForm.classList.add('visible');
        showQuestion(currentQuestion);
        questionForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 1000);
    });
  
    nextBtn.addEventListener('click', () => {
      const selected = document.querySelector('input[name="answer"]:checked');
      if (!selected) {
        alert("Пожалуйста, выберите вариант ответа");
        return;
      }
      nextBtn.disabled = true;
      const data = {
        question: questions[currentQuestion].title,
        answer: selected.value
      };
      fetch('/save-answer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Ошибка при сохранении ответа');
        }
        return response.json();
      })
      .then(result => {
        console.log('Ответ сохранён', result);
        if (currentQuestion < questions.length - 1) {
          currentQuestion++;
          showQuestion(currentQuestion);
          nextBtn.disabled = false;
        } else {
          questionForm.innerHTML = "<h2>Сейчас узнаем кто может стать вашим новым другом!</h2>";
        }
      })
      .catch(error => {
        console.error('Ошибка:', error);
        alert("Произошла ошибка при сохранении ответа. Попробуйте ещё раз.");
        nextBtn.disabled = false;
      });
    });
  });
  