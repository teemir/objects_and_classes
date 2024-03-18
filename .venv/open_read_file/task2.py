def create_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = ingredients
            f.readline()  # Пропуск пустой строки между блюдами
    return cook_book

file_path = 'recipes.txt'  # Путь к файлу с рецептами
cook_book = create_cook_book(file_path)
print(cook_book)
# Проверка
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shopping_list)