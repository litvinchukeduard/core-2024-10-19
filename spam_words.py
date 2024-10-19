import re
'''
Написати функцію, яка буде отримувати текст і прибирати з нього усі спам-слова

Python, PytHon, python, PythoN

москаль Мoскaль москалЬ

"Москаль прийшов, щось натворив"
"москаль прийшов, щось натворив"
"москаЛь прийшов, щось натворив"
"МОСКАЛЬ прийшов, щось натворив"

"****** прийшов, щось натворив"
'''

spam_word_list = [
    "МОСКАЛЬ"
]

def to_lowercase(text: str) -> str:
    return text.lower()

def replace_spam_words(text: str) -> str:
    lowercase_text = to_lowercase(text)
    for spam_word in spam_word_list:
        spam_word_lowercase = to_lowercase(spam_word)
        text = re.sub(spam_word_lowercase, '*' * len(spam_word), lowercase_text)
        # result.span
    return text


# print('*' * 7)
text = "москаЛь прийшов, щось натворив"
print(replace_spam_words(text))
