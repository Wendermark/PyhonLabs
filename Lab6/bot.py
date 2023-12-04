import telebot
import telebot.types as types
import random

import database

bot = telebot.TeleBot('6799792060:AAHXAjcep_D3h-Jr-Q9FKWw39rhe92e84Og')

questions = [
    ("Как называется самая большая пустыня в мире?", ["Сахара", "Гоби", "Атакама", "Антарктида"]),
    ("Какой химический элемент имеет символ Fe?", ["Железо", "Фтор", "Фосфор", "Фермий"]),
    ("Кто написал роман «Война и мир»?", ["Лев Толстой", "Федор Достоевский", "Михаил Булгаков", "Александр Пушкин"]),
    ("Какая страна является самой маленькой по площади в мире?", ["Ватикан", "Монако", "Науру", "Сан-Марино"]),
    ("Какой океан омывает западное побережье Австралии?", ["Индийский", "Тихий", "Атлантический", "Южный"]),
    ("Какое животное является национальным символом Канады?", ["Бобр", "Лось", "Орел", "Медведь"]),
    ("Какой город является столицей Японии?", ["Токио", "Осака", "Киото", "Хиросима"]),
    ("Какой фрукт является самым популярным в мире по объему производства?", ["Банан", "Яблоко", "Апельсин", "Томат"]),
    ("Какой спорт считается национальным в Индии?", ["Крикет", "Хоккей", "Футбол", "Бадминтон"]),
    ( "Какой из этих фильмов получил Оскар за лучший фильм в 2020 году?", ["Паразиты", "1917", "Джокер", "Однажды в Голливуде"]),
    ( "Какой из этих художников родился в Нидерландах?", ["Винсент ван Гог", "Пабло Пикассо", "Леонардо да Винчи", "Клод Моне"]),
    ( "Какой из этих языков является официальным в Швейцарии?", ["Немецкий", "Французский", "Итальянский", "Все перечисленные"]),
    ( "Какой из этих математических терминов означает умножение двух чисел?", ["Произведение", "Сумма", "Разность", "Частное"]),
    ( "Какой из этих писателей известен своими детективными романами?", ["Агата Кристи", "Джордж Оруэлл", "Джон Рональд Руэл Толкин", "Джеймс Джойс"]),
    ( "Какой из этих органов человека отвечает за кроветворение?", ["Костный мозг", "Селезенка", "Печень", "Поджелудочная железа"]),
    ( "Какой из этих музыкальных инструментов относится к духовым?", ["Саксофон", "Скрипка", "Гитара", "Барабан"]),
    ( "Какой из этих цветов является вторичным?", ["Зеленый", "Красный", "Синий", "Желтый"]),
    ( "Какой из этих континентов является самым населенным в мире?", ["Азия", "Африка", "Европа", "Америка"]),
    ( "Какой из этих планет является самой большой в Солнечной системе?", ["Юпитер", "Сатурн", "Уран", "Нептун"]),
    ( "Какой из этих видов искусства связан с использованием красок?", ["Живопись", "Скульптура", "Гравюра", "Каллиграфия"]),
]

quiz_state = {}

def start_quiz(chat_id):

    randomQuestionId = random.randint(0, len(quiz_state[chat_id]["questions"]) - 1) 

    randomQuestion = quiz_state[chat_id]["questions"][randomQuestionId]

    question, rightAnswer, answers = randomQuestion[0], randomQuestion[1][0], randomQuestion[1]

    quiz_state[chat_id]["questioniD"] = randomQuestionId
    quiz_state[chat_id]["answer"] = rightAnswer

    random.shuffle(answers)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    for a in answers:
        keyboard.add(a)

    bot.send_message(chat_id, question, reply_markup= keyboard)

def check_answer(chat_id, user_answer):

    correct_answer = quiz_state[chat_id]["answer"]

    if user_answer.lower() == "stop":

        bot.send_message(chat_id, f"Вы остановили викторину, ваш счет - {quiz_state[chat_id]['score']}", reply_markup=types.ReplyKeyboardRemove())

        database.save_score(chat_id, quiz_state[chat_id]["score"])

        return

    if user_answer.lower() == correct_answer.lower():
        
        del quiz_state[chat_id]["questions"][quiz_state[chat_id]["questioniD"]]

        bot.send_message(chat_id, 'Верно!')

        quiz_state[chat_id]["score"] = quiz_state[chat_id]["score"] + 1

        if len(quiz_state[chat_id]["questions"]) == 0:

            bot.send_message(chat_id, f"Вы победили в викторине! Ваш счет - {quiz_state[chat_id]['score']}")

            database.save_score(chat_id, quiz_state[chat_id]["score"])

            return
    else:

        bot.send_message(chat_id, f'Неверно. Правильный ответ: {correct_answer}')

    start_quiz(chat_id)

@bot.message_handler(commands=['start'])
def handle_start(message):

    chat_id = message.chat.id

    database.register_user(message.from_user.id, message.from_user.username)

    bot.send_message(chat_id, 'Привет! Я бот-викторина. Я задам тебе несколько вопросов, а ты должен ответить на них. Начнем? Для отмены напиши stop')

    quiz_state[chat_id] = { }

    quiz_state[chat_id]["questions"] = questions

    quiz_state[chat_id]["score"] = 0

    start_quiz(chat_id)

@bot.message_handler(commands=['stats'])
def handle_start(message):

    chat_id = message.chat.id

    stats = database.get_top_score()

    msg = ""

    for s in stats:
        msg += f"Имя - {s[1]} Счет - {s[2]}\n"

    bot.send_message(chat_id, msg)


@bot.message_handler(content_types=['text'])
def handle_text(message):

    chat_id = message.chat.id

    user_answer = message.text

    if chat_id in quiz_state:

        check_answer(chat_id, user_answer)
    else:
        bot.send_message(chat_id, 'Чтобы начать викторину, введите команду /start')

bot.polling()