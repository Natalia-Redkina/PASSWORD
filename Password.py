import string # импортирует модуль для работы с общими строковыми операциями
import random # импортирует модуль, реализующий генераторы случайных чисел для различных распределений
import datetime # импортирует модуль, предоставляющий классы для работы с датами и временем
import re # импортируем модуль, предоставляющий операции с регулярными выражениями
# определяем переменные
dt = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") # для имен файлов input_fname = "task_file.txt"
error_fname = f"error_file.{dt}.csv"
result_fname = f"result_file.{dt}.csv"
result_header = "EMAIL;NAME;LAST_NAME;TEL;CITY;PASSWORD"
pwd_len = 12
min_name_length = 2
min_surname_length = 2
min_city_length = 2
min_uniq_digit_in_number = 2
def input_validation(user_data):
"""Функция проверяет корректность данных"""
name = user_data[1] surname = user_data[2] number = user_data[3] city = user_data[4]
# проверяем имя, фамилию, город по единой логике, они должны начинаться с заглавной буквы, заканчиваться строчной и иметь длину не менее двух символов
if len(name) < min_name_length or len(surname) < min_surname_length or len(city) < min_city_length:
return False
if name[0].islower() or surname[0].islower() or city[0].islower():
return False
if name[-1].isupper() or surname[-1].isupper() or city[-1].isupper():
return False
# проверяем номер телефона
if re.search("^\d+$", number): # базовая проверка, проверяет, чтобы номер телефона состоял только из цифр
if len(set(number)) < min_uniq_digit_in_number: # вторичная проверка, проверяет чтобы номер телефона состоял не менее, чем из двух уникальных цифр
return False else:
return True else:
return False return True
def email_gen(list_of_names):
"""Функция создает почтовые адреса"""
emails = []
for i in list_of_names:
letter = 1
while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
letter += 1
emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
return emails
def gen_pswd(Pwd_len):
"""Функция генерирует пароль"""
L = list("{0}{1}{2}".format(string.punctuation, string.digits, string.ascii_letters)) random.shuffle(L)
password = [random.choice(L) for _ in range(8)] +
list(random.choice(string.punctuation)) + list(
random.choice(string.digits)) + list(random.choice(string.ascii_lowercase)) + list( random.choice(string.ascii_uppercase))
   random.shuffle(password)

return ''.join(password)[0:Pwd_len]
result = []
name_surname = []
# заполняем титульную строку, содержащую название граф with open(result_fname, 'a') as the_file:
the_file.write(result_header + "\n")
# Создаем список содержащий валидные данные
with open(input_fname) as f: for line in f:
user_data = line.rstrip().split(",")
user_data[1] = user_data[1].replace(" ", "") # нормализуем имя user_data[2] = user_data[2].replace(" ", "") # нормализуем фамилию user_data[3] = user_data[3].replace(" ", "") # нормализуем номер
if input_validation(user_data): # сохраняем в массив валидные данные
name = user_data[1]
surname = user_data[2] name_surname.append([name, surname]) result.append(user_data)
else: # записываем в файл данные с ошибками with open(error_fname, 'a') as the_file:
the_file.write(';'.join(user_data) + "\n") email_list = email_gen(name_surname)
# обогащаем валидные данные почтой и паролем, сохраняем в результирующий файл
n=0
for user_data in result:
user_data[0] = email_list[n] user_data.append(gen_pswd(pwd_len).replace(";", "x")) user_data_str = ';'.join(user_data)
with open(result_fname, 'a') as the_file:
the_file.write(user_data_str + "\n") n += 1

