open('v.txt') as cook_book:
    for line in cook_book:
        name = line
        col = cook_book.readline()
        ing = cook_book.readline()
        col_ing = cook_book.readline()
        name_ing = cook_book.readline()




def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['col_ing'] *= person_count
      if new_shop_list_item['name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['name']]['col_ing'] += new_shop_list_item['col_ing']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['name'], shop_list_item['col_ing'],
                            shop_list_item['name_ing']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
