# Programm the "The gallows game"

from random import *

import time

word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар',
             'территория', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'население', 'большинство',
             'музыка', 'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
             'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ', 'журнал', 'руководитель', 'специалист',
             'оценка', 'регион', 'процент', 'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
             'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
             'граница', 'модель', 'операция', 'название', 'старик', 'миллион', 'счастье', 'ребята', 'кабинет',
             'магазин', 'пространство', 'знание', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник',
             'участок', 'желание', 'доктор', 'председатель', 'представление', 'солдат', 'художник', 'оружие',
             'соответствие', 'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга', 'содержание',
             'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сотрудник', 'предложение', 'технология',
             'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'продукция', 'техника',
             'здание', 'необходимость', 'подготовка', 'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
             'обстоятельство', 'победа', 'источник', 'звезда', 'сестра', 'практика', 'проведение', 'карман',
             'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан', 'работник', 'обеспечение',
             'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'теория', 'разработка', 'личность',
             'праздник', 'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель', 'множество',
             'особенность', 'показатель', 'корабль', 'впечатление', 'частность', 'детство', 'профессор', 'прошлое',
             'командир', 'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка', 'заявление', 'попытка', 'сравнение',
             'расчет', 'депутат', 'комитет', 'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
             'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица', 'механизм',
             'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'сожаление', 'заместитель',
             'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист', 'фигура', 'субъект', 'реакция',
             'список', 'фотография', 'журналист', 'нарушение', 'заседание', 'больница', 'существо', 'свойство',
             'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник', 'реализация', 'страница',
             'формирование', 'житель', 'красота', 'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
             'университет', 'традиция', 'декабрь', 'ладонь', 'сведение', 'цветок', 'октябрь', 'занятие', 'сентябрь',
             'помещение', 'январь', 'зритель', 'редакция', 'фактор', 'август', 'известие', 'зависимость', 'охрана',
             'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция', 'переход', 'произведение',
             'родина', 'собственность', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'клиент', 'отрасль',
             'беседа', 'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение', 'понимание', 'апрель',
             'кодекс', 'настроение', 'должность', 'преступление', 'лестница', 'установка', 'появление', 'получение',
             'образец', 'главное', 'костюм', 'ценность', 'обязанность', 'таблица', 'воспоминание', 'лошадь', 'коллега',
             'организм', 'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение', 'оборона', 'выступление',
             'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан', 'километр', 'признак',
             'промышленность', 'американец', 'заключение', 'восток', 'исключение', 'постановление', 'перевод',
             'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина',
             'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка', 'изучение', 'просьба', 'публика', 'сообщение',
             'угроза', 'достижение', 'назначение', 'реклама', 'портрет', 'стакан', 'творчество', 'телевизор',
             'инструмент', 'концепция', 'лейтенант', 'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
             'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство', 'вещество',
             'категория', 'гостиница', 'издание', 'объединение', 'темнота', 'человечество', 'колесо', 'опасность',
             'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат', 'родственник', 'давление',
             'присутствие', 'взаимодействие', 'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание', 'оплата',
             'разница', 'водитель', 'снижение', 'формула', 'капитал', 'новость', 'эффект', 'губернатор', 'доклад',
             'убийство', 'эксперт', 'автобус', 'платье', 'общение', 'психология', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
             'признание', 'постель', 'владелец', 'компьютер', 'инженер', 'старуха', 'ракета', 'вершина', 'выпуск',
             'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность', 'талант', 'эффективность', 'полоса',
             'основное', 'рассмотрение', 'следователь', 'описание', 'редактор', 'дворец', 'забота', 'столик',
             'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'дружба',
             'окончание', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кредит', 'господь',
             'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'металл', 'молоко', 'прокурор',
             'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
             'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король', 'подъезд', 'автомат', 'мальчишка',
             'чтение', 'поселок', 'свидетель', 'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение', 'статус',
             'параметр', 'сказка', 'тенденция', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'эксплуатация',
             'коммунист', 'пенсия', 'приятель', 'объяснение', 'производитель', 'философия', 'мощность', 'обязательство',
             'кризис', 'указание', 'яблоко', 'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
             'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица', 'обработка', 'чемпионат']

error_words = ['Не то печатаешь, давай заново',
               'Что печатаешь, двоечник! Заново',
               'Ошибка. Пробуй заново',
               'Кто тебя учил текст набирать? Удаляю и снова печатай',
               'Неверный текст, снова давай',
               'Галиматья, опять давай',
               'Чушь! Нет таких букв в алфавите. Снова давай']

guessed_list = ['Ты уже писал такое. Напряги извилины',
                'Тебе надо на свежий воздух. То же самое пишешь',
                'Было уже. Попробуй еще',
                'Опять! было уже',
                'Что заладил одно и то же. Давай думай еще',
                'Нет. Было уже. Еще варианты']

guess_words = ['Есть такая буква', 'Угадал букву']

not_guess_letter = ['Нет такой буквы', 'Вот и не угадал', 'Не угадал', 'Не та буква',
                    'Подумай еще и начни с другой буквы', 'Нет. Не выдумывай']

not_guess_words = ['Нет такого слова', 'Вот и не угадал', 'Не угадал', 'Не то слово',
                   'Хватит себя мучить. Угадывай буквы', 'Нет. Не выдумывай']

win_words = ['Выиграл! Красавчик! ', 'Угадал, Дай пять! Хотя нет, можешь нажать пять раз [Enter]',
             'Ты разгадал! Всеми правдами и неправдами ты сделал это']

approval = ['да', 'продолжай', 'lf', 'д', 'l', 'дп', 'lg']

again = 'l'

start = True


def display_hangman(tries):
    stages = ['''
                 ________
                 |/     |
                 |      O
                 |     \\|/
                 |      |
                 |    _/ \\_
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |     \\|/
                 |      |
                 |    _/ \\
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |     \\|/
                 |      |
                 |     /
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |     \\|/
                 |      |
                 |
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |     \\|
                 |      |
                 |
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |      |
                 |      |
                 |
                 -
              ''',
              '''
                 ________
                 |/     |
                 |      O
                 |
                 |
                 |
                 -
              ''',
              '''
                 ________
                 |/     |
                 |
                 |
                 |
                 |
                 -
              ''',
              '''
                 ________
                 |/
                 |
                 |
                 |
                 |
                 -
              ''',
              '''
                 ________
                 |
                 |
                 |
                 |
                 |
                 -
              ''',
              '''

                 |
                 |
                 |
                 |
                 |
                 -
              ''',
              '''






                 -
              '''
              ]
    return stages[tries]


def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def get_word():
    return choice(word_list)


def rules():
    print('\nДавайте играть в угадайку слов! Или же игру "Виселица"!\n')
    print(
        'Ваша задача - отгадать слово до того, как будет дорисован человечек на виселице.\n'
        'Вы может вводить буквы (по одной за раз) или слово целиком.\n'
        'Вы можете ошибиться до 12 раз, в зависимости от выбранного вами уровня сложности.')


def play(text):
    word_completion = '_' * len(text)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    if start:
        rules()
    while True:  # Уровень сложности игры
        level = input(
            '\nВыберете уровень сложности: легкий (12 допустимых ошибок), средний (8), сложный (6) (1/2/3): ').strip()
        if level == '1':
            tries = 12
            break
        elif level == '2':
            tries = 8
            break
        elif level == '3':
            tries = 6
            break
        else:
            print('\nНужно ввести "1", "2" или "3"!')
    # Подсказка
    show_letters = input('\nПоказать первую и последнюю буквы? ').lower()
    if show_letters in approval:
        word_completion = text[0] + word_completion[1:-1] + text[-1]
    print('...Загрузка игры...\n')
    s = '|'
    for i in range(26):
        time.sleep(0.05)
        print('\r', i * s, str(i * 4), '%', end='')
    print()
    print(display_hangman(8))
    print(word_completion)
    print()
    while not guessed and tries > 0:
        guess = input('Введите букву или слово целиком: ').lower()
        if len(guess) == 1 and guess.isalpha():  # Если ввели букву
            if guess in guessed_letters:
                print(choice(guessed_list))
            elif guess not in text:
                print(choice(not_guess_letter))
                tries -= 1
                print(f'Вы не угадали букву, осталось попыток {tries}')
                guessed_letters.append(guess)
            else:
                print('\nОтличная работа, буква', guess, 'присутствует в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(text)) if text[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(text) and guess.isalpha():  # Если ввели слово целиком
            if guess in guessed_words:
                print(choice(win_words))
            elif guess != text:
                print(choice(not_guess_words))
                tries -= 1
                print(f'Вы не угадали слово, осталось попыток {tries}')
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = text
        else:
            print(choice(error_words))
        if level == '3':
            print(display_hangman(tries + 2))
        else:
            print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + text.upper() + '. Может быть в следующий раз!')


while again.lower() in approval:
    word = get_word()
    play(word)
    again = input('Играем еще раз? ')
    start = False
else:
    print('Приходи в следующий раз!')
