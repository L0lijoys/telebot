import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('api botfather')

#Внимание! ТЕЛЕБОТ ВЫПОЛНЯЕТ КОМАНДЫ СВЕРХУ-ВНИЗ. Если найдёт совпадение того, что выполнит его команду - он её выполнит и больше не будет искать похожие или ответ. Дубликаты он не делает!#
@bot.message_handler(commands=['start']) #с помощью месседж хендлер, мы ставим фильтр и задачу боту. Например, при написании Старт /start, он выполнит команду внизу#
def started(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 3)
    knopka2 = types.KeyboardButton(text='Команды бота')
    knopka3 = types.KeyboardButton(text='Бросить кубик')
    knopka4 = types.KeyboardButton(text='Играть в дартс')
    knopka5 = types.KeyboardButton(text='Играть в казино')
    knopka6 = types.KeyboardButton(text='Играть в футбол')
    knopka7 = types.KeyboardButton(text='Играть в казино')
    knopka8 = types.KeyboardButton(text='Играть в баскетбол')
    knopka9 = types.KeyboardButton(text='Играть в боулинг')
    knopka10 = types.KeyboardButton(text='Доступные игры')

    markup.add(knopka2, knopka3, knopka4, knopka5, knopka6, knopka7, knopka8, knopka9, knopka10)
    namepeople = f'Привет,<b>{message.from_user.first_name}.</b> Бот Випсеков V.1.1 запущен🤟. Чтобы посмотреть список команд, напиши Команды бота или нажми кнопку бота.'
    bot.send_message(message.chat.id, namepeople, parse_mode='html', reply_markup=markup)

# ______________________
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Вот список моих команд: \n/start - начало работы,\n/aboutus - об авторах,\n/chattype - узнать тип чата,\n", parse_mode='html')
@bot.message_handler(commands=['vicodin'])
def vicodin(message):
    bot.send_message(message.chat.id,message)
#обработчик message с данными vicodin сверху
@bot.message_handler(commands=['chattype'])
def chattype(message):
    typechat1 = f'Тип чата: <b>{message.chat.type}</b>'
    bot.send_message(message.chat.id, typechat1, parse_mode='html')

#_____________________блок кнопок и реакции________________________


@bot.message_handler(content_types=['text'])
def buttonblock(message):
    if message.text == 'Саня берет в рот':
        bot.send_message(message.chat.id, 'Полностью поддерживаю')
    elif message.text == 'Авторы бота':
        bot.send_message(message.chat.id, "В главных ролях: твоя мама, Хью Лорри, горбатый змей Максим, татаро-монгольское иго и нацист Алексей. А также, все VIPсеки!", parse_mode='html')
    elif message.text == 'Тип чата':
        typechat1 = f'Тип чата: <b>{message.chat.type}</b>'
        bot.send_message(message.chat.id, typechat1, parse_mode='html')
    elif message.text == 'Команды бота':
        bot.send_message(message.chat.id, "С нашей первой встречи, я стал умнее🤟.\n Я больше не использую команды и реагирую на слова и фразы: \n 1)Команды бота - посмотреть список команд.\n 2)Авторы бота - посмотреть авторов бота. \n 3)Саня берет в рот - подтверждение фактов.\n 4)Тип чата - проверить тип чата\n 5)Доступные игры - посмотреть доступные мини-игры. ")
    elif message.text == 'Бросить кубик':
        bot.send_dice(message.chat.id, '🎲')
    elif message.text == 'Играть в дартс':
        bot.send_dice(message.chat.id, '🎯')
    elif message.text == 'Играть в казино':
        bot.send_dice(message.chat.id, '🎰')
    elif message.text == 'Играть в футбол':
        bot.send_dice(message.chat.id, '⚽')
    elif message.text == 'Играть в баскетбол':
        bot.send_dice(message.chat.id, '🏀')
    elif message.text == 'Играть в боулинг':
        bot.send_dice(message.chat.id, '🎳')
    elif message.text == 'Доступные игры':
        bot.send_message(message.chat.id, 'Доступные игры:\n "Бросить кубик"\n "Играть в дартс"\n "Играть в казино"\n "Играть в футбол"\n "Играть в баскетбол"\n "Играть в боулинг"\n Чтобы начать любую игру, напиши её название без кавычек с большой буквы, или используй кнопки бота в чате. (не работает с веб-версией телеграмм)')

bot.polling(none_stop= True)