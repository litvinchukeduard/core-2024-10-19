import re
'''
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.


Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.


Для виконання завдання візьміть наступний приклад лог-файлу:

2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.

yyyy-mm-dd hh:mm:ss LEVEL Message


Вимоги до завдання:

    Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
    Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
    Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
    Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
    Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
    Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
    Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
    Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.
'''

# 1) Відкрити файл та прочитати з нього усі логи
# 2) З кожного логу дістати дату, рівень та повідомлення та зберегти

def read_logs_from_file(path: str) -> list[str]:
    with open(path, 'r') as log_file:
        return log_file.readlines()
    
def parse_logs(logs: list[str]):
    result_list = []
    for log in logs:
        named_log_pattern = r'(?P<date_time>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>[\w \.]+)'
        result_list.append(re.search(named_log_pattern, log).groupdict())
    return result_list


logs = read_logs_from_file('2024-10-19|12-14.log')
parsed_logs = parse_logs(logs)

for log in parsed_logs:
    print(log['level'])

# print(read_logs_from_file('2024-10-19|12-14.log'))
# # print("2024-01-22 08:30:01 INFO User logged in successfully.".split(' '))

# log_string = "2024-01-22 08:30:01 INFO User logged in successfully."
# date_pattern = r'\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}'
# # print(re.search(date_pattern, log_string).group())

# log_pattern = r'(\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (\w+)'

# named_log_pattern = r'(?P<date_time>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>[\w \.]+)'

# print(re.search(named_log_pattern, log_string).groupdict())

# m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')

# print(m.groupdict())
