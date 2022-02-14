def open_file():
    cook_book = {}
    with open('reciept.txt', encoding='utf-8') as file:
        for line in file:
            key = line.strip()
            list_ing = []
            for i in range(int(file.readline().strip())):
                value = file.readline().strip()
                split_value = value.split(' | ')
                dict_ing = {'ingredient_name': split_value[0], 'quantity': split_value[1], 'measure': split_value[2]}
                list_ing.append(dict_ing)
            file.readline()
            cook_book[key] = list_ing
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        ingredients = open_file()[dish]
        for ingredient in ingredients:
            ingredient['quantity'] = int(ingredient['quantity']) * person_count
        print(dish, *ingredients, sep='\n')


print(open_file())
print()
get_shop_list_by_dishes(['Омлет', 'Омлет'], 5)
