# заводим счетчик = 0
# откроем файл
# циклом пройдем по строкам файла
# # проверяем удовлетворяет ли строка условию
# # # увеличиваем счетчик, печатаем строку
# закрыть файл
# вывести счетчик

count = 0
with open('warandpeace.txt', encoding="utf-8") as file:
    for line in file:
        if 'Пьер' in line and 'Наташ' in line:
            count += 1
            print(line.rstrip())
            print('====')

print(f'Пьер и Наташа упоминались вместе {count} раз')
