import random

# Выводим текст приветствия пользователю
print('Добро пожаловать в числовую угадайку\n')

# Функция проверки корректности введённых данных
def is_valid(txt, upper_limit):
    try:
        int_txt = int(txt)
        # если переданный аргумент txt является целым числом от 1 до n, то вернёт True 
        return 1 <= int_txt <= upper_limit
    except ValueError:
        # в противном случае вернёт False
        return False

def get_user_input(upper_limit, attempt_count):
    # Создаём цикл, который запрашивает у пользователя данные и выводит их
    while True:
        attempt_count += 1 # подсчёт количества попыток
        user_input = input(f'Введите целое число от 1 до {upper_limit}: ') 
        if not is_valid(user_input, upper_limit):
            print(f'А может быть всё-таки введём целое число от 1 до {upper_limit}?') # если данные некорректны
        else:
            return int(user_input), attempt_count # если данные корректны, то преобразуем их к целому числу для удобства дальнейшей работы

# Создаём функцию генерации случайного числа от 1 до n, где устанавливаем правую границу для ввода пользователю и числом по умолчанию 
def play_game(upper_limit = 100):
    target_number = random.randint(1, upper_limit) #генерация случайного числа
    attempt_count = 0 #начало счётчика для подсчёта количества попыток
    # guessed булевая переменная, которая указывает угадал ли пользователь загаданное число
    # изначально устанавливаем значение False, что означает, что число ещё не угадано
    guessed = False

    # цикл продолжается до тех пор, пока guessed остаётся False
    while not guessed:
        number, attempt_count = get_user_input(upper_limit, attempt_count)
        print(f'Введённое Вами число: {number}')

        if number < target_number:
            print(f'Ваше число {number} меньше загаданного, попробуйте еще разок')
        elif number > target_number:
            print(f'Ваше число {number} больше загаданного, попробуйте еще разок')
        else:
            # если число угадано, устаналиваем guessed в True, чтобы завершить цикл и выводим сообщение
            print(f'Вы угадали, поздравляем!\nВведённое Вами число {number} совпадает с загаданным числом {target_number}')
            guessed = True

    print(f'\nКоличество попыток: {attempt_count}')
    print('\nПоздравляю! Вы угадали число. Хотите сыграть ещё раз? (Да/Нет)')
    # создаём переменную choise, которая будет хранить выбор пользователя: играть ещё раз или закончить игру
    choice = input().lower()
    # если пользователь выбрал 'Да', предлагаем ему начать новую игру с новой границей 
    if choice == 'да':
        new_upper_limit = int(input('Введите новую верхнюю границу (по умолчанию 100): ') or 100)
        play_game(new_upper_limit)
    else:
        # если пользователь выбрал 'Нет', благодарим его за участие и заканчиваем игру
        print('\nСпасибо, что играли в числовую угадайку. Еще увидимся...')

upper_limit = int(input('Введите верхнюю границу для случайного выбора числа (по умолчанию 100): ') or 100)
play_game(upper_limit)