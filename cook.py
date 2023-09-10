cook_book = {}
with open('ingridients.txt', encoding='utf-8') as f:
    dish_name = None
    ingredients_list = []

    for line in f:
        line = line.strip()

        if not line:
            continue

        if dish_name is None:
            dish_name = line
            continue

        if line.isdigit():
            ingredients_qty = int(line)
            continue

        ingredient_info = line.split("|")
        if len(ingredient_info) != 3:
            continue

        ingredient_name, quantity, measure = ingredient_info
        ingredient_dict = {
            'ingredient_name': ingredient_name.strip(),
            'quantity': quantity.strip(),
            'measure': measure.strip()
        }
        ingredients_list.append(ingredient_dict)

    cook_book[dish_name] = ingredients_list

print(cook_book)
print(dish_name)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients_list = cook_book[dish]

            for ingredient_info in ingredients_list:
                ingredient_name = ingredient_info['ingredient_name']
                quantity = int(ingredient_info['quantity']) * person_count
                measure = ingredient_info['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'quantity': quantity,
                        'measure': measure
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        else:
            print(f"Блюдо {dish} не найдено в кулинарной книге.")

    return shop_list



