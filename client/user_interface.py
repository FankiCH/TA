from telebot import types
import telebot
import webbrowser



# аааааааааааааааааааааааа

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Информационный')
    keyboard1.row(button1)
    button2 = types.KeyboardButton(text='Образовательный')
    button3 = types.KeyboardButton(text= 'Развлекательный')
    keyboard1.row(button2, button3)
    bot.send_message(message.chat.id, 'Привет, этот чат бот поможет тебе в создании видеоконтента. Он расскажет, как вести себя в кадре, напишет сценарий'
                                      ', может сгенерировать видеоролик и создать картинку для превью.')
    bot.send_message(message.chat.id, 'Для более точного создания контента, я задам вам несколько вопросов. Какой тип видеоконтента вы хотите снимать?', reply_markup = keyboard1)
    bot.register_next_step_handler(message, question1)


def question1(message):
    step = False
    if message.text.lower() == 'информационный':
        bot.send_message(message.chat.id, 'Inf')
        step = True
    elif message.text.lower() == 'образовательный':
        step = True
        bot.send_message(message.chat.id, 'обр')
    elif message.text.lower() == 'развлекательный':
        step = True
        bot.send_message(message.chat.id, 'play')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Короткое видео(рилс, шортс)')
        keyboard1.row(button1)
        button2 = types.KeyboardButton(text='Видеоблог')
        button3 = types.KeyboardButton(text='Видео для ютуба')
        keyboard1.row(button2, button3)
        bot.send_message(message.chat.id, 'В каком формате вы хотите снимать видеоролики?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question2)

def question2(message):
    step = False
    if message.text.lower() == 'короткое видео(рилс, шортс)':
        bot.send_message(message.chat.id, 'shortVideo')
        step = True
    elif message.text.lower() == 'видеоблог':
        bot.send_message(message.chat.id, 'video_blog')
        step = True
    elif message.text.lower() == 'видео для ютуба':
        bot.send_message(message.chat.id, 'YouTube')
        step = True
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Да, буду')
        button2 = types.KeyboardButton(text='Нет, не буду')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Будете  ли вы участвовать в кадре?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question3)


def question3(message):
    step = False
    if message.text.lower() == 'да, буду':
        bot.send_message(message.chat.id, 'presence_in_frame')
        step = True
    elif message.text.lower() == 'нет, не буду':
        bot.send_message(message.chat.id, 'absence_in_frame')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Да, нужна')
        button2 = types.KeyboardButton(text='Нет, не нужна')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Нужна ли вам подробная информация, как вести себя в кадре?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question4)
    elif step == False:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Да, нужен')
        button2 = types.KeyboardButton(text='Нет, не нужен')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Нужен ли вам подробный сценарий?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question6)

def question4(message):
    step = False
    if message.text.lower() == 'да, нужна':
        bot.send_message(message.chat.id, 'instruction_frame')
        step = True
    elif message.text.lower() == 'нет, не нужна':
        bot.send_message(message.chat.id, 'Хорошо, понял вас')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Да, я умею настраивать свет')
        button2 = types.KeyboardButton(text='Нет, не умею')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Умеете ли вы настраивать правильно свет в кадре?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question5)

    else:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Да, нужен')
        button2 = types.KeyboardButton(text='Нет, не нужен')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Нужен ли вам подробный сценарий?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question6)


def question5(message):
    step = False
    if message.text.lower() == 'да, я умею настраивать свет':
        bot.send_message(message.chat.id, 'light_not_needed')
        step = True

    elif message.text.lower() == 'нет, не умею':
        bot.send_message(message.chat.id, 'light_needed')

    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Да, нужен')
    button2 = types.KeyboardButton(text='Нет, не нужен')
    keyboard1.row(button1, button2)
    bot.send_message(message.chat.id, 'Нужен ли вам подробный сценарий?', reply_markup=keyboard1)
    bot.register_next_step_handler(message, question6)

def question6(message):
    step = False
    if message.text.lower() == 'да, нужен':
        bot.send_message(message.chat.id, 'script_needed')
        step = True
    elif message.text.lower() == 'нет, не нужен':
        step = True
        bot.send_message(message.chat.id, 'script_not_needed')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text='Требуется')
        button2 = types.KeyboardButton(text='Не требуется')
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, 'Требуется ли помощь в создании рекламы?', reply_markup=keyboard1)
        bot.register_next_step_handler(message, question7)

def question7(message):
    step = False
    if message.text.lower() == 'требуется':
        bot.send_message(message.chat.id, 'advertisement_needed')
        step = True
    elif message.text.lower() == 'не требуется':
        step = True
        bot.send_message(message.chat.id, 'advertisement_not_needed')
    if step:
        bot.send_message(message.chat.id, 'И последние, кратко опишите, о чём вы хотите создать видео(название, тема, суть)')
        bot.register_next_step_handler(message, question8)





@bot.message_handler(commands=['getInfo'])
def het_info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Ссылка на наш сайт", url="https://github.com/Mishailian/TA")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Информация о проекте", reply_markup=keyboard)

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Перейти в гугл', url='https://www.google.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def question8(message):
    idea = bot.reply_to(message, f"Ваша идея для видео: {message.text}")
    #bot.send_message(message.chat.id, f"Ваша идея для видео: {idea}")
    bot.send_message(message.chat.id, 'Работа над вашим видеороликом началась, подождите...')

if __name__ =="__main__":
    bot.infinity_polling()



















































