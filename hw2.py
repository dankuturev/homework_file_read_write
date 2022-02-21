def open_file():
    cook_book = {}
    with open('reciept.txt') as file:
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
    ing_list = {}
    for dish in dishes:
        ingredients = open_file()[dish]
        for ingredient in ingredients:
            key = ingredient['ingredient_name']
            if key in ing_list.keys():
                ing_list[key]['quantity'] *= 2
            else:
                ing_list[key] = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
    return print(ing_list)


print(open_file())
print()
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
