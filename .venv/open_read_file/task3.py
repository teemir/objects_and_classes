
files_data = []
file_names = ["1.txt", "2.txt", "3.txt"]

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        files_data.append((file_name, len(lines), "".join(lines)))

# Сортируем содержимое файлов по количеству строк
files_data.sort(key=lambda num_line: num_line[1])

# Записываем содержимое файлов в результирующий файл
with open("result.txt", 'w', encoding='utf-8') as result_file:
    for file_data in files_data:
        result_file.write(f"{file_data[0]}\n{file_data[1]}\n{file_data[2]}\n")
