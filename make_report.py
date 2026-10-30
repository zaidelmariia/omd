# ДЗ Функии

# В `Corp_Summary.csv` лежит выгрузка по сотрудникам: ФИО, департамент, команда, должность, оценка, оклад. Колонки разделены `;`.

# Напишите программу, которая читает файл и по выбранному в аргументах варианту готовит отчёт. На экран выводите так, как вам удобно читать.

# Варианты отчётов такие. Основная функция должна принимать на вход int - номер варианта. остальные параметры - по желанию:

# 1. Иерархия: для каждого департамента показать, какие команды в него входят.
# 2. Сводка по департаментам: название, сколько человек, минимальная и максимальная зарплата, средняя по каждому департаменту.
# 3. То же самое, что в "2", но записанное в csv-файл. Имя выходного файла можно захардкодить(например, константой в начале файла) или передавать опциональным параметром в эту же функцию.

# Чтение файла и каждый отчёт вынесите в отдельные функции.



import csv
import argparse

def read_csv(name: str) -> list[list[str]]:
    with open(name, encoding='utf-8', newline='') as file:
            
            reader = csv.reader(file, delimiter=';')
            res = []

            for row in reader:
                res.append(row)

            return res

def hierarchy_report(table:list[list[str]]):
    '''Печатает иерархию компании: список отделов каждого департамента
    На вход принимает список списков строк - распакованную таблицу с информацией о сотрудниках
    '''
    dep_pos = 0
    unit_pos = 0
    for i in range(len(table[0])):
        if table[0][i] == 'Департамент':
            dep_pos = i
        if table[0][i] == 'Отдел':
            unit_pos = i
    #print(dep_pos, unit_pos)

    dep_set = set([str[dep_pos] for str in table[1:]])

    dep_unit_dict = {dep:set() for dep in dep_set}

    for str in table[1:]:
        dep_unit_dict[str[dep_pos]].add(str[unit_pos])

    print ('-------------------')
    print ('ИЕРАРХИЯ')
    for dep in dep_unit_dict:
        print(f'{dep}: {', '.join(dep_unit_dict[dep])}')
    print ('-------------------')


def salary_report_dict(table:list[list[str]]) -> dict[str,list[int]]:
    '''
    Готовит сводку по департаментам в виде словаря для дальнейшего использования
    На вход принимает список списков строк - распакованную таблицу с информацией о сотрудниках
    Возвращает словарь, где ключ - название департамента, значение - список из четырех значений по этому департаменту:
    [0] - число сотрудников, [1] - минимальная ЗП, [2] - максимальная ЗП, [3]- средняя ЗП
    '''
    dep_pos = 0
    sal_pos = 0
    for i in range(len(table[0])):
        if table[0][i] == 'Департамент':
            dep_pos = i
        if table[0][i] == 'Оклад':
            sal_pos = i
    
        
    dep_set = set([str[dep_pos] for str in table[1:]])    
    
    dep_salary_dict = {dep:[0,0,0,0] for dep in dep_set} 
    #в списке будем хранить: [0]-число сотрудников, [1]-минимальная ЗП, [2]-максимальная ЗП, 
    # [3]-сумма всех ЗП, которую затем разделим на число сотрудников и получим среднее

    for str in table[1:]:
        dep_salary_dict[str[dep_pos]][0] +=1
        if dep_salary_dict[str[dep_pos]][1] != 0 and int(str[sal_pos]) < dep_salary_dict[str[dep_pos]][1] or dep_salary_dict[str[dep_pos]][1] == 0:
            dep_salary_dict[str[dep_pos]][1] = int(str[sal_pos])
        if int(str[sal_pos]) > dep_salary_dict[str[dep_pos]][2]:
            dep_salary_dict[str[dep_pos]][2] = int(str[sal_pos])
        dep_salary_dict[str[dep_pos]][3] += int(str[sal_pos])

    
    for dep in dep_salary_dict:
        dep_salary_dict[dep][3] = round(dep_salary_dict[dep][3] / dep_salary_dict[dep][0])
        
    return dep_salary_dict
   
def salary_report(table:list[list[str]]):
    '''
    Печатает сводку по департаментам: количество сотрудников, диапазон зарплат и среднюю зарплата по департаменту
    На вход принимает список списков строк - распакованную таблицу с информацией о сотрудниках
    '''
    dep_salary_dict = salary_report_dict(table)

    print ('-------------------')    
    print('СВОДКА ПО ДЕПАРТАМЕНТАМ')
    for dep in dep_salary_dict: 
        print (f'{dep}: {dep_salary_dict[dep][0]} сотрудников, зарплата варьируется от {dep_salary_dict[dep][1]} до {dep_salary_dict[dep][2]} со средним значением {dep_salary_dict[dep][3]}')
    print ('-------------------')

    return dep_salary_dict

def salary_report_csv(table:list[list[str]], file_name = 'salary_report.csv'):

    '''
    Записывает в файл типа .csv сводку по департаментам: количество сотрудников, диапазон зарплат и среднюю зарплата по департаменту
    На вход принимает список списков строк - распакованную таблицу с информацией о сотрудниках
    Опционально - название файла для записи
    По дефолту записывает результат в файл salary_report.csv
    '''
    dep_salary_dict = salary_report_dict(table)

    with open(file_name, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
        'Департамент',
        'Количество сотрудников',
        'Минимальная зарплата',
        'Максимальная зарплата',
        'Средняя зарплата'
        ])
        for dep, stats in dep_salary_dict.items():
            writer.writerow([dep, *stats])

        print ('-------------------')  
        print(f'Сводка по департаментам записана в файл {file_name}')
        print ('-------------------')  




def make_report(r_type: int, input_file_name: str = 'Corp_Summary.csv', output_file_name: str = 'salary_report.csv'):
    '''
    Готовит отчет по файлу одного из трех типов:
    1 - Иерархия: департаменты и входящие в них отделы
    2 - Сводка по департаментам: количество сотрудников, диапазон зарплат и средняя зарплата по департаменту
    3 - Сводка по департаментам, записанная в .csv-файл
    '''
    
    if r_type == 1:
        hierarchy_report(read_csv(input_file_name))
    elif r_type == 2:
        salary_report(read_csv(input_file_name))
    elif r_type == 3:
        salary_report_csv(read_csv(input_file_name), output_file_name)    
   


def main():
    '''
    Основная функция, которая парсит аргументы командной строки и вызывает функцию make_report
    '''

    default_input_file = 'Corp_Summary.csv'
    default_output_file = 'salary_report.csv'
    
    parser = argparse.ArgumentParser(
        description='Первый аргумент - номер типа отчета: ' \
        '1 - Иерархия: департаменты и входящие в них отделы; ' \
        '2 - Сводка по департаментам: количество сотрудников, диапазон зарплат и средняя зарплата по департаменту; ' \
        '3 - Сводка по департаментам, записанная в .csv-файл. ' \
        'Второй аргумент (опционально) - название файла для чтения. ' \
        'Третий аргумент (опционально) - название файла для записи. '
    )



    parser.add_argument(
        'report_type',
        help='Номер типа отчета: 1, 2 или 3',
        type=int,
        choices=[1, 2, 3]
    )

    parser.add_argument(
        '--input-file',
        help='Название файла для чтения',
        type=str,
        default=default_input_file
    )

    parser.add_argument(
        '--output-file',
        type=str,
        help='Название файла для записи (только для отчета 3)',
        default=default_output_file
    )


    args = parser.parse_args()

    r_type = args.report_type
    input_file = args.input_file
    output_file = args.output_file

    if not args.input_file.lower().endswith('.csv'):
        parser.error('Входной файл должен иметь расширение .csv')

    if not args.output_file.lower().endswith('.csv'):
            parser.error('Выходной файл должен иметь расширение .csv')

    make_report(r_type, input_file, output_file)



if __name__ == "__main__":
    main()