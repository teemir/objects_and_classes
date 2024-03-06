
with open('hello.txt', 'rt', encoding="utf-8") as fp:
    for line in fp:
        print(line.rstrip())
        print('=====')


print(f'Файл закрыт? {fp.closed}')

