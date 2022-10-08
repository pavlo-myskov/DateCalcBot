from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from relativedelta_parser import parse_relativedelta

'''
Быстрый подсчет
Считает к-во лет-месяцев-недель-дней-часов-минут в зависимости от размера диапазона
Пользователь вводит две даты через знак тире между ними, и получает быстрый результат
'''


def quick_count(user_input_string: str) -> str:
    '''
    Принимает строку от юзера, парсит, вычисляет, и возвращает результат в виде строки
    Пример строки от юзера: `20.05.2003 23:15 - 14 Jan 2018`
    Пример вывода: `Years: 14, Months: 7, Days: 24, Minutes: 45`
    '''
    try:
        first, second = user_input_string.split('-')
    except Exception as e:
        print('Problem with spliting the user_input_string', type(e.__name__), e)
        return 'Wrong format, the dash `-` must only be strictly between the dates'
    else:
        try:
            start = parse(first, dayfirst=True)
        except Exception as e:
            print('First part of the user_input_string if wrong',
                  type(e.__name__), e)
            return 'Wrong format of your start date/time'
        else:
            try:
                end = parse(second, dayfirst=True)
            except Exception as e:
                print('First part of the user_input_string if wrong',
                      type(e.__name__), e)
                return 'Wrong format of your end date/time'
            else:
                try:
                    delta = relativedelta(end, start)
                except Exception as e:
                    print('relativedelta', type(e.__name__), e)
                    return 'Wrong input, try again'
                else:
                    output_list = parse_relativedelta(delta)
                    return ', '.join(output_list)


# print(quick_count('20.05.2003 23:15 - 14 Jan 2018'))