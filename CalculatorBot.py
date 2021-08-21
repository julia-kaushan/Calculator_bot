import telebot

HELP = """Доступные команды:
/help - напечатать справку 
/calc - решает пример
"""

print('Start telegram bot...')

token = '1756878692:AAGEO-Q91RLUq1VIKDP3iG9modF6SI8EnG4'
bot = telebot.TeleBot(token)


def part_of_example(message):
    example = message.text[6:].split(' ')
    a = int(example[0])
    b = int(example[-1])
    operator = example[1]
    return a, b, operator


def summa(a, b):
    return a + b


def division(a, b):
    if b == 0:
        return 'На ноль делить нельзя!'
    return a / b


def difference(a, b):
    return a - b


def multiplication(a, b):
    return a * b


operators = {'+': summa, '-': difference, '*': multiplication, '/': division}


# /help
@bot.message_handler(commands=['help'])
def help_todo(message):
    bot.send_message(message.chat.id, HELP)

# /calc
@bot.message_handler(commands=['calc'])
def calculator(message):
    """Реши пример"""
    a, b, operator = part_of_example(message)
    result = operators[operator](a, b)
    bot.send_message(message.chat.id, f'Ответ на пример: {result}')


bot.polling(none_stop=True)
