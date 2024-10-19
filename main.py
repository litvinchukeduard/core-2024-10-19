"""
Вимоги до завдання:

    (Коректність реалізації функції fibonacci(n) з урахуванням використання кешу. Ефективне використання рекурсії та кешування для оптимізації обчислень.)
    1.Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n). (5 балів)
    2. fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу. (5 балів)
    3.Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат. (5 балів)
    4.Використання рекурсії для обчислення чисел Фібоначчі. (5 балів)
 
    
    5.Чистота коду, включаючи читабельність та наявність коментарів. (5 балів)
"""

def my_function(number: int) -> str:
    """My function to do something"""
    return